# -*- coding: utf-8 -*-
"""
generate_lecture_ai.py
Runs image-grounded AI generation for a specific lecture (L4, L5, or L6).
Saves to cache_{lecture}.json incrementally.
"""

import os
import sys
import json
import time
import re
import subprocess

AGY_EXE = os.environ.get("ANTIGRAVITY_AGENTAPI_EXE", r"C:\Users\smane\.gemini\bin\agy.exe")

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

def call_ai_for_slide(image_path, lecture_code, page_num):
    cfg = LECTURE_CONFIGS[lecture_code]
    prompt = f"""You are a world-class semiconductor process engineer and cleanroom materials professor.
Carefully inspect the slide image at '{image_path}'.
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
        
    return clean_json_output(res.stdout)

def run_lecture(lecture_code):
    if lecture_code not in LECTURE_CONFIGS:
        print(f"Unknown lecture code: {lecture_code}")
        return
        
    cfg = LECTURE_CONFIGS[lecture_code]
    cache_file = f"cache_{lecture_code.lower()}.json"
    cache = {}
    
    if os.path.exists(cache_file):
        try:
            with open(cache_file, "r", encoding="utf-8") as f:
                cache = json.load(f)
            print(f"[{lecture_code}] Loaded {len(cache)} existing cached slides from {cache_file}")
        except Exception as e:
            print(f"[{lecture_code}] Error loading cache: {e}")
            cache = {}
            
    # Also check ai_slides_cache.json for any pre-existing slides
    if os.path.exists("ai_slides_cache.json"):
        try:
            with open("ai_slides_cache.json", "r", encoding="utf-8") as f:
                master_cache = json.load(f)
            for k, v in master_cache.items():
                if k.startswith(lecture_code) and k not in cache:
                    if v.get("explanationTh") and len(v["explanationTh"]) > 150:
                        cache[k] = v
        except Exception:
            pass

    total = cfg["total"]
    print(f"[{lecture_code}] Total slides: {total} | Currently cached: {len(cache)}")
    
    for page in range(1, total + 1):
        slide_id = f"{lecture_code}-P{page:03d}"
        if slide_id in cache:
            entry = cache[slide_id]
            if entry.get("explanationTh") and len(entry["explanationTh"]) > 180 and "สไลด์นี้อธิบายเนื้อหาหัวข้อ" not in entry["explanationTh"]:
                continue
                
        image_path = f"images/{lecture_code}_page_{page}.png"
        if not os.path.exists(image_path):
            print(f"[{lecture_code}] Image not found: {image_path}, skipping!")
            continue
            
        max_retries = 3
        success = False
        for attempt in range(1, max_retries + 1):
            try:
                t0 = time.time()
                data = call_ai_for_slide(image_path, lecture_code, page)
                dt = time.time() - t0
                
                if not data.get("explanationTh") or len(data["explanationTh"]) < 80:
                    raise ValueError("Explanation too short or missing")
                    
                cache[slide_id] = data
                with open(cache_file, "w", encoding="utf-8") as f:
                    json.dump(cache, f, ensure_ascii=False, indent=2)
                    
                print(f"[{lecture_code}] [{page:03d}/{total:03d}] SUCCESS {slide_id} in {dt:.1f}s | {data.get('titleEn', '')}", flush=True)
                success = True
                break
            except Exception as e:
                print(f"[{lecture_code}] [{page:03d}/{total:03d}] ATTEMPT {attempt} FAILED for {slide_id}: {e}", flush=True)
                time.sleep(2 * attempt)
                
        if not success:
            print(f"[{lecture_code}] PERMANENT FAILURE for {slide_id}", flush=True)

    print(f"[{lecture_code}] FINISHED! Total slides in cache: {len(cache)} / {total}", flush=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_lecture_ai.py <L4|L5|L6>")
        sys.exit(1)
    lec = sys.argv[1].upper()
    run_lecture(lec)
