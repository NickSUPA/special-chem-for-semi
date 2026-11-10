# -*- coding: utf-8 -*-
"""
fast_gemini_generator.py
High-throughput multimodal slide generation using Gemini API keys.
Generates in-depth technical explanations for all slides in L4, L5, L6.
"""

import os
import sys
import json
import time
import base64
import re
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

API_KEYS = [k.strip() for k in os.environ.get("GEMINI_API_KEYS", "").split(",") if k.strip()]
if not API_KEYS:
    # Fallback to single GEMINI_API_KEY if defined
    if os.environ.get("GEMINI_API_KEY"):
        API_KEYS = [os.environ.get("GEMINI_API_KEY")]

MODELS = [
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-3-flash-preview",
    "gemini-3.8-flash",
    "gemini-2.5-pro"
]

LECTURE_CONFIGS = {
    "L4": {
        "title": "Lecture 4: Specialty Chemicals & Gases for Semiconductor Fabrication",
        "titleTh": "บทที่ 1 & 2: สารเคมีและก๊าซพิเศษในกระบวนการผลิตอุปกรณ์สารกึ่งตัวนำ (Facilities, UPW, Gases, Etch)",
        "total": 133,
        "defaultCategory": "Fab Infrastructure & Specialty Gases",
        "defaultCategoryTh": "โครงสร้างพื้นฐานและก๊าซพิเศษใน Fab"
    },
    "L5": {
        "title": "Lecture 5: Specialty Gases and Chemicals for Lithography Process",
        "titleTh": "บทที่ 3: ก๊าซและสารเคมีพิเศษสำหรับกระบวนการโฟโตลิโทกราฟี (Photoresists, DUV, EUV, Track)",
        "total": 105,
        "defaultCategory": "Photolithography Chemicals & Materials",
        "defaultCategoryTh": "เคมีภัณฑ์และวัสดุสำหรับกระบวนการลิโทกราฟี"
    },
    "L6": {
        "title": "Lecture 6: CMP Chemicals (Chemical Mechanical Planarization)",
        "titleTh": "บทที่ 4: สารเคมีสำหรับกระบวนการขัดผิวเชิงกลและเคมี (CMP Slurries, Post-CMP Cleaning)",
        "total": 64,
        "defaultCategory": "CMP Chemicals & Slurry Engineering",
        "defaultCategoryTh": "เคมีภัณฑ์และวิศวกรรมสเลอร์รี่สำหรับ CMP"
    }
}

file_locks = {
    "L4": threading.Lock(),
    "L5": threading.Lock(),
    "L6": threading.Lock()
}

key_index = 0
key_index_lock = threading.Lock()

MEM_CACHE = {
    "L4": {},
    "L5": {},
    "L6": {}
}

def init_mem_cache():
    for lec in ["L4", "L5", "L6"]:
        fname = f"cache_{lec.lower()}.json"
        if os.path.exists(fname):
            try:
                with open(fname, "r", encoding="utf-8") as f:
                    MEM_CACHE[lec] = json.load(f)
            except Exception as e:
                print(f"Warning loading {fname}: {e}")
                MEM_CACHE[lec] = {}
        # Also incorporate master cache
        if os.path.exists("ai_slides_cache.json"):
            try:
                with open("ai_slides_cache.json", "r", encoding="utf-8") as f:
                    m = json.load(f)
                for k, v in m.items():
                    if k.startswith(lec) and is_slide_complete(v):
                        if k not in MEM_CACHE[lec] or not is_slide_complete(MEM_CACHE[lec].get(k)):
                            MEM_CACHE[lec][k] = v
            except Exception:
                pass

def save_slide_to_cache(lecture_code, slide_id, slide_data):
    fname = f"cache_{lecture_code.lower()}.json"
    tmp_fname = f"{fname}.tmp"
    with file_locks[lecture_code]:
        MEM_CACHE[lecture_code][slide_id] = slide_data
        # Atomic write
        with open(tmp_fname, "w", encoding="utf-8") as f:
            json.dump(MEM_CACHE[lecture_code], f, ensure_ascii=False, indent=2)
        os.replace(tmp_fname, fname)

def get_next_api_key():
    global key_index
    with key_index_lock:
        k = API_KEYS[key_index % len(API_KEYS)]
        key_index += 1
        return k

def clean_json_output(raw_text):
    text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        text = match.group(1).strip()
    else:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end != -1:
            text = text[start:end+1]
    
    try:
        return json.loads(text)
    except Exception:
        cleaned = re.sub(r",\s*([\]}])", r"\1", text)
        return json.loads(cleaned)

def call_gemini_multimodal(image_path, lecture_code, page_num):
    cfg = LECTURE_CONFIGS[lecture_code]
    with open(image_path, "rb") as f:
        img_b64 = base64.b64encode(f.read()).decode("utf-8")

    prompt = f"""You are a world-class semiconductor process engineer and cleanroom materials professor.
Carefully inspect this slide image from '{cfg['title']}', Slide Page {page_num}.
Extract and explain all visual and textual elements shown in the image with extreme technical accuracy.
Do not make generic summaries. Directly explain the visual content of the slide (diagrams, tables, chemical formulas, reactions, equipment schematics, operational principles, flowcharts, and exact numerical specs).

Output ONLY valid JSON with this exact schema:
{{
  "titleEn": "Precise English title from the slide",
  "titleTh": "ชื่อหัวข้อภาษาไทยที่กระชับและตรงตามศัพท์เทคนิคเซมิคอนดักเตอร์",
  "category": "{cfg['defaultCategory']}",
  "categoryTh": "{cfg['defaultCategoryTh']}",
  "summaryTh": "สรุปเนื้อหาสาระสำคัญของภาพนี้เป็นภาษาไทย 2-3 ประโยค",
  "explanationTh": "คำอธิบายเชิงลึกภาษาไทยอย่างละเอียด อธิบายทุกองค์ประกอบ แผนภาพ ตาราง แผนภูมิ ขั้นตอน ปฏิกิริยาเคมี หรือตัวเลขที่ปรากฏในภาพให้ครบถ้วน จัดรูปแบบให้อ่านง่าย มีหัวข้อข้อย่อย",
  "keyPoints": [
    "ประเด็นสำคัญทางเทคนิคที่ 1 ที่ปรากฏในภาพ",
    "ประเด็นสำคัญทางเทคนิคที่ 2 ที่ปรากฏในภาพ",
    "ประเด็นสำคัญทางเทคนิคที่ 3 ที่ปรากฏในภาพ"
  ],
  "formula": "สูตรเคมี สมการปฏิกิริยา หรือความสัมพันธ์ทางคณิตศาสตร์ในภาพ (ถ้าไม่มีให้ใส่สตริงว่าง)",
  "examTip": "จุดเน้นสำหรับการสอบหรือกฎเหล็กการทำงานจริงใน Fab ที่เกี่ยวข้องกับภาพนี้"
}}
"""

    payload = {
        "contents": [{
            "parts": [
                {"inline_data": {"mime_type": "image/png", "data": img_b64}},
                {"text": prompt}
            ]
        }],
        "generationConfig": {
            "responseMimeType": "application/json",
            "temperature": 0.2
        }
    }

    max_attempts = 8
    last_err = None

    for attempt in range(max_attempts):
        key = get_next_api_key()
        model = MODELS[attempt % len(MODELS)]
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"

        try:
            r = requests.post(url, json=payload, headers={"Content-Type": "application/json"}, timeout=35)
            if r.status_code == 200:
                res_data = r.json()
                text = res_data["candidates"][0]["content"]["parts"][0]["text"]
                parsed = clean_json_output(text)
                if parsed.get("explanationTh") and len(parsed["explanationTh"]) >= 80:
                    return parsed, model
                else:
                    raise ValueError("Explanation too short or missing")
            elif r.status_code in [429, 503]:
                last_err = f"{r.status_code} on {model}: {r.text[:80]}"
                time.sleep(2.0 + attempt * 1.5)
            else:
                last_err = f"{r.status_code} on {model}: {r.text[:100]}"
                time.sleep(1.0)
        except Exception as e:
            last_err = str(e)
            time.sleep(1.5 + attempt * 1.0)

    raise RuntimeError(f"All {max_attempts} attempts failed. Last error: {last_err}")

def is_slide_complete(slide_entry):
    if not slide_entry or not isinstance(slide_entry, dict):
        return False
    exp = slide_entry.get("explanationTh", "").strip()
    if len(exp) < 100 or "สไลด์นี้อธิบายเนื้อหาหัวข้อ" in exp:
        return False
    return True

def process_slide_task(task_info):
    lecture = task_info["lecture"]
    page = task_info["page"]
    slide_id = task_info["id"]
    image_path = task_info["image"]

    t0 = time.time()
    try:
        data, model = call_gemini_multimodal(image_path, lecture, page)
        dt = time.time() - t0
        save_slide_to_cache(lecture, slide_id, data)
        return {
            "id": slide_id,
            "lecture": lecture,
            "page": page,
            "success": True,
            "dt": dt,
            "model": model,
            "title": data.get("titleTh", "")
        }
    except Exception as e:
        dt = time.time() - t0
        return {
            "id": slide_id,
            "lecture": lecture,
            "page": page,
            "success": False,
            "dt": dt,
            "model": None,
            "error": str(e)
        }

def run_generation(target_lectures=None, max_workers=6):
    init_mem_cache()

    if target_lectures is None:
        target_lectures = ["L4", "L5", "L6"]
    else:
        target_lectures = [l.upper() for l in target_lectures]

    tasks = []
    total_slides_count = 0
    cached_count = 0

    for lec in target_lectures:
        cfg = LECTURE_CONFIGS[lec]
        total = cfg["total"]
        total_slides_count += total

        for p in range(1, total + 1):
            sid = f"{lec}-P{p:03d}"
            img = f"images/{lec}_page_{p}.png"
            if not os.path.exists(img):
                continue

            if sid in MEM_CACHE[lec] and is_slide_complete(MEM_CACHE[lec][sid]):
                cached_count += 1
                continue

            tasks.append({
                "lecture": lec,
                "page": p,
                "id": sid,
                "image": img
            })

    print("=" * 60)
    print(f"FAST MULTIMODAL GEMINI GENERATOR (MEMORY-BACKED ATOMIC CACHE)")
    print(f"API Keys available: {len(API_KEYS)}")
    print(f"Workers: {max_workers}")
    print(f"Target lectures: {', '.join(target_lectures)}")
    print(f"Total slides in scope: {total_slides_count}")
    print(f"Already high quality in cache: {cached_count}")
    print(f"Remaining tasks to process: {len(tasks)}")
    print("=" * 60)

    if not tasks:
        print("All slides are already complete and high quality!")
        import subprocess
        subprocess.run(["python", "merge_and_build.py"])
        return

    completed_in_run = 0
    failed_tasks = []

    t_start = time.time()
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_slide_task, task): task for task in tasks}

        for future in as_completed(futures):
            res = future.result()
            sid = res["id"]
            lec = res["lecture"]
            page = res["page"]
            total_lec = LECTURE_CONFIGS[lec]["total"]

            if res["success"]:
                completed_in_run += 1
                curr_cached = cached_count + completed_in_run
                pct = (curr_cached / total_slides_count) * 100.0
                print(f"[{lec}] [{page:03d}/{total_lec:03d}] [Total {curr_cached}/{total_slides_count} ({pct:.1f}%)] SUCCESS {sid} in {res['dt']:.1f}s ({res['model']}) | {res['title']}", flush=True)
            else:
                failed_tasks.append(futures[future])
                print(f"[{lec}] [{page:03d}/{total_lec:03d}] FAILED {sid}: {res.get('error')}", flush=True)

    elapsed = time.time() - t_start
    print("=" * 60)
    print(f"GENERATION RUN FINISHED in {elapsed:.1f}s ({elapsed/60:.2f} min)")
    print(f"Successfully generated: {completed_in_run} / {len(tasks)}")
    if failed_tasks:
        print(f"Failed count: {len(failed_tasks)} (Re-running them now...)")
        with ThreadPoolExecutor(max_workers=2) as retry_executor:
            retry_futures = {retry_executor.submit(process_slide_task, task): task for task in failed_tasks}
            for rf in as_completed(retry_futures):
                r_res = rf.result()
                print(f"RETRY RESULT {r_res['id']}: success={r_res['success']}")

    print("Running final merge_and_build.py...")
    import subprocess
    subprocess.run(["python", "merge_and_build.py"])
    print("All done!")

if __name__ == "__main__":
    lecs = sys.argv[1:] if len(sys.argv) > 1 else None
    run_generation(lecs, max_workers=6)
