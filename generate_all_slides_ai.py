# -*- coding: utf-8 -*-
"""
generate_all_slides_ai.py
Generates detailed, image-grounded technical explanations in Thai for all 302 slides
across Lecture 4, Lecture 5, and Lecture 6 using Gemini multimodal vision.
"""

import os
import sys
import json
import time
import re
import threading
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed

AGY_EXE = os.environ.get("ANTIGRAVITY_AGENTAPI_EXE", r"C:\Users\smane\.gemini\bin\agy.exe")
CACHE_FILE = "ai_slides_cache.json"
MAX_WORKERS = 2  # Safe, rock-solid concurrency

LECTURES = [
    {
        "code": "L4",
        "title": "Lecture 4: Specialty Chemicals & Gases for Semiconductor Fabrication",
        "titleTh": "บทที่ 1 & 2: สารเคมีและก๊าซพิเศษในกระบวนการผลิตอุปกรณ์สารกึ่งตัวนำ (Facilities, UPW, Gases, Etch)",
        "total": 133
    },
    {
        "code": "L5",
        "title": "Lecture 5: Specialty Gases and Chemicals for Lithography Process",
        "titleTh": "บทที่ 3: ก๊าซและสารเคมีพิเศษสำหรับกระบวนการโฟโตลิโทกราฟี (Photoresists, DUV, EUV, Track)",
        "total": 105
    },
    {
        "code": "L6",
        "title": "Lecture 6: CMP Chemicals (Chemical Mechanical Planarization)",
        "titleTh": "บทที่ 4: สารเคมีสำหรับกระบวนการขัดผิวเชิงกลและเคมี (CMP Slurries, Post-CMP Cleaning)",
        "total": 64
    }
]

cache_lock = threading.Lock()
cache_data = {}

def load_cache():
    global cache_data
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                cache_data = json.load(f)
            print(f"[CACHE] Loaded {len(cache_data)} cached slides from {CACHE_FILE}")
        except Exception as e:
            print(f"[CACHE] Error loading cache: {e}. Starting fresh.")
            cache_data = {}
    else:
        cache_data = {}

def save_cache():
    with cache_lock:
        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(cache_data, f, ensure_ascii=False, indent=2)

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

def call_ai_vision_for_slide(image_path, lecture_code, page_num):
    prompt = f"""You are a world-class semiconductor process engineer and cleanroom materials professor.
Carefully inspect the slide image at '{image_path}'.
Extract and explain all visual and textual elements shown in the image with extreme technical accuracy.
Do not make generic summaries. Directly explain the visual content of the slide (diagrams, tables, chemical formulas, reactions, equipment schematics, operational principles, flowcharts, and exact numerical specs).

Output ONLY valid JSON with this exact schema:
{{
  "titleEn": "Precise English title from the slide",
  "titleTh": "ชื่อหัวข้อภาษาไทยที่กระชับและตรงตามศัพท์เทคนิคเซมิคอนดักเตอร์",
  "category": "Category in English (e.g. Fab Infrastructure, UPW, Deposition Gases, Lithography, CMP, etc.)",
  "categoryTh": "หมวดหมู่ภาษาไทย",
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
    cmd = [
        AGY_EXE,
        "--model", "gemini-3.8-flash-low",
        "--effort", "low",
        "--dangerously-skip-permissions",
        "-p", prompt
    ]
    
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
    except subprocess.TimeoutExpired:
        raise RuntimeError("Subprocess timed out after 60 seconds")
        
    if res.returncode != 0:
        raise RuntimeError(f"agy process exited with {res.returncode}: {res.stderr}")
        
    parsed = clean_json_output(res.stdout)
    return parsed

def process_single_slide(slide_meta):
    slide_id = slide_meta["id"]
    
    # Check cache
    with cache_lock:
        if slide_id in cache_data:
            existing = cache_data[slide_id]
            if existing.get("explanationTh") and len(existing["explanationTh"]) > 180 and "สไลด์นี้อธิบายเนื้อหาหัวข้อ" not in existing["explanationTh"]:
                return slide_id, True, 0.0, "Cached"
                
    image_path = slide_meta["image"]
    lecture_code = slide_meta["lecture"]
    page_num = slide_meta["page"]
    
    max_retries = 3
    last_err = None
    for attempt in range(1, max_retries + 1):
        try:
            t0 = time.time()
            ai_result = call_ai_vision_for_slide(image_path, lecture_code, page_num)
            dt = time.time() - t0
            
            if not ai_result.get("explanationTh") or len(ai_result["explanationTh"]) < 80:
                raise ValueError("Explanation too short or missing")
                
            with cache_lock:
                cache_data[slide_id] = ai_result
                save_cache()
                
            return slide_id, True, dt, ai_result.get("titleEn", "")
        except Exception as e:
            last_err = e
            time.sleep(2 * attempt)
            
    return slide_id, False, 0.0, str(last_err)

def assemble_slides_data(tasks):
    final_slides = []
    for t in tasks:
        sid = t["id"]
        c = cache_data.get(sid, {})
        
        slide_obj = {
            "id": sid,
            "lecture": t["lecture"],
            "lectureTitle": t["lectureTitle"],
            "lectureTitleTh": t["lectureTitleTh"],
            "page": t["page"],
            "totalPages": t["totalPages"],
            "titleEn": c.get("titleEn", sid),
            "titleTh": c.get("titleTh", sid),
            "category": c.get("category", "Semiconductor Manufacturing"),
            "categoryTh": c.get("categoryTh", "การผลิตสารกึ่งตัวนำ"),
            "image": t["image"],
            "rawText": "",
            "summaryTh": c.get("summaryTh", ""),
            "explanationTh": c.get("explanationTh", ""),
            "keyPoints": c.get("keyPoints", []),
            "formula": c.get("formula", ""),
            "examTip": c.get("examTip", "")
        }
        final_slides.append(slide_obj)
        
    js_content = f"// Autogenerated Slide Database for TMEC Specialty Chemicals & Gases (302 Slides AI-Generated Complete)\n"
    js_content += f"// Lectures: L4 (133 slides), L5 (105 slides), L6 (64 slides)\n"
    js_content += f"window.ALL_SLIDES = {json.dumps(final_slides, ensure_ascii=False, indent=2)};\n"
    
    with open("slides_data.js", "w", encoding="utf-8") as f:
        f.write(js_content)
        
    print(f"[COMPLETE] Wrote slides_data.js successfully! Total: {len(final_slides)} slides. Size: {len(js_content)/1024:.1f} KB")

def main():
    load_cache()
    
    tasks = []
    print("[INIT] Building task list for 302 slides...")
    for lec in LECTURES:
        for p in range(1, lec["total"] + 1):
            slide_id = f"{lec['code']}-P{p:03d}"
            image_path = f"images/{lec['code']}_page_{p}.png"
            tasks.append({
                "id": slide_id,
                "lecture": lec["code"],
                "lectureTitle": lec["title"],
                "lectureTitleTh": lec["titleTh"],
                "page": p,
                "totalPages": lec["total"],
                "image": image_path
            })
            
    total_slides = len(tasks)
    assert total_slides == 302, f"Expected 302 slides, got {total_slides}"
    
    already_done = 0
    for t in tasks:
        sid = t["id"]
        if sid in cache_data and len(cache_data[sid].get("explanationTh", "")) > 180 and "สไลด์นี้อธิบายเนื้อหาหัวข้อ" not in cache_data[sid]["explanationTh"]:
            already_done += 1
            
    print(f"[STATUS] Total slides: {total_slides} | Already cached: {already_done} | Remaining to generate: {total_slides - already_done}")
    
    if already_done == total_slides:
        print("[SUCCESS] All 302 slides already generated in cache!")
        assemble_slides_data(tasks)
        return

    print(f"[RUN] Starting generation with {MAX_WORKERS} workers...")
    completed_count = already_done
    start_time = time.time()
    
    # Process with thread pool
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_map = {executor.submit(process_single_slide, t): t for t in tasks}
        for future in as_completed(future_map):
            sid, success, dt, info = future.result()
            if success:
                if info != "Cached":
                    completed_count += 1
                    elapsed = time.time() - start_time
                    percent = (completed_count / total_slides) * 100
                    print(f"[{completed_count:03d}/{total_slides}] ({percent:.1f}%) SUCCESS {sid} in {dt:.1f}s | {info}", flush=True)
            else:
                print(f"[ERROR] Failed {sid}: {info}", flush=True)

    # Retry pass for any missing slides
    missing = [t for t in tasks if t["id"] not in cache_data or not cache_data[t["id"]].get("explanationTh") or len(cache_data[t["id"]]["explanationTh"]) < 80]
    if missing:
        print(f"[RETRY] Retrying {len(missing)} missing or incomplete slides...", flush=True)
        with ThreadPoolExecutor(max_workers=2) as retry_exec:
            retry_map = {retry_exec.submit(process_single_slide, t): t for t in missing}
            for future in as_completed(retry_map):
                sid, success, dt, info = future.result()
                if success and info != "Cached":
                    completed_count += 1
                    percent = (completed_count / total_slides) * 100
                    print(f"[{completed_count:03d}/{total_slides}] ({percent:.1f}%) RETRY SUCCESS {sid} in {dt:.1f}s | {info}", flush=True)

    print(f"[FINISH] All tasks completed. Assembling final slides_data.js...", flush=True)
    assemble_slides_data(tasks)

if __name__ == "__main__":
    main()
