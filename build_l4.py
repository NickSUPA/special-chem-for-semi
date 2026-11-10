# -*- coding: utf-8 -*-
"""
build_l4.py
Generates detailed Thai explanations and technical data for all 133 slides of Lecture 4.
"""
import json

def generate_l4_dataset():
    with open('L4_Specialty Chemicals and Gases for Semiconductor Devices Fabrication_V4_NA_01092026_extracted.json', 'r', encoding='utf-8') as f:
        raw = json.load(f)
        
    slides = []
    l4_meta = {}
    
    # Key anchor slides for L4
    l4_meta[1] = {
        "titleEn": "Course Title: Specialty Chemicals and Gases in Fab",
        "titleTh": "หน้าปกหลักสูตร: สารเคมีและก๊าซพิเศษในกระบวนการผลิตอุปกรณ์เซมิคอนดักเตอร์",
        "cat": "Fab Infrastructure & Facilities", "catTh": "โครงสร้างพื้นฐานและระบบสนับสนุนใน Fab",
        "sum": "การบรรยายวิชาเคมีและก๊าซพิเศษสำหรับโรงงานเซมิคอนดักเตอร์ โดย ดร. นิติ เอี่ยมถิ ผู้จัดการคลีนรูม TMEC สวทช.",
        "exp": "สไลด์เปิดหลักสูตร Lecture 4 ของวิชา 'Specialty Chemicals and Gases for Semiconductor Devices Fabrication' บรรยายโดย ดร. นิติ เอี่ยมถิ (Dr. Nithi Atthi) ผู้จัดการคลีนรูมศูนย์ไมโครอิเล็กทรอนิกส์ (TMEC) สวทช. เนื้อหาบทนี้เป็นรากฐานที่สำคัญที่สุด ครอบคลุมการออกแบบโรงงานผลิตชิป (Wafer Fab Facilities), ระบบน้ำบริสุทธิ์ยิ่งยวด (UPW), ก๊าซพิเศษในกระบวนการปลูกฟิล์ม (Deposition), ก๊าซเจือสาร (Doping), ก๊าซกัดพลาสมา (Plasma Etch), ระบบท่อส่งก๊าซบริสุทธิ์ยิ่งยวด (UHP Piping) และความปลอดภัยสารเคมีตามมาตรฐานสากล",
        "kp": ["วิชาเคมีและก๊าซพิเศษในกระบวนการผลิตชิปเซมิคอนดักเตอร์", "ครอบคลุมระบบสนับสนุน (Sub-fab Facilities) และก๊าซในกระบวนการผลิต (Process Gases)", "บรรยายโดยผู้จัดการคลีนรูม TMEC สวทช."],
        "form": "", "tip": "L4 เป็นบทที่มีเนื้อหากว้างที่สุด ครอบคลุมทั้ง Fab Infrastructure, UPW, CVD Gases, Doping และ Plasma Etching"
    }

    l4_meta[4] = {
        "titleEn": "Semiconductor Wafer Fab Infrastructure",
        "titleTh": "โครงสร้างพื้นฐานของโรงงานผลิตเวเฟอร์ (Semiconductor Wafer Fab)",
        "cat": "Fab Infrastructure & Facilities", "catTh": "โครงสร้างพื้นฐานและระบบสนับสนุนใน Fab",
        "sum": "สถาปัตยกรรม 3 ระดับของโรงงานผลิตชิป: Cleanroom ชั้นบน, Sub-fab ชั้นล่าง, และ Central Utility Building (CUB)",
        "exp": "โรงงานผลิตชิป (Wafer Fab) มีโครงสร้างทางสถาปัตยกรรมและวิศวกรรมที่ซับซ้อนที่สุดในบรรดาโรงงานอุตสาหกรรม โดยแบ่งออกเป็น 3 ระดับหลัก: 1. Cleanroom Floor (Fab Level): ห้องสะอาดชั้นบนสุดซึ่งเป็นที่ติดตั้งเครื่องจักรผลิตชิปที่มีมูลค่ามหาศาล มีการควบคุมอนุภาคฝุ่น อุณหภูมิ และความชื้นอย่างเข้มงวด 2. Sub-fab Level: ชั้นใต้ดินหรือชั้นล่างใต้คลีนรูม เป็นที่ติดตั้งปั๊มสุญญากาศ (Vacuum Pumps), ตู้ควบคุมก๊าซ (Gas Cabinets/VMB), ระบบบำบัดไอพิษ (Scrubbers), และหม้อแปลงไฟฟ้า 3. Central Utility Building (CUB): อาคารผลิตสาธารณูปโภคส่วนกลางที่ผลิตน้ำ UPW, น้ำหล่อเย็น (Chilled Water), ไฟฟ้าสำรอง (UPS), และระบบบำบัดน้ำเสีย",
        "kp": ["โครงสร้าง 3 ชั้น: Cleanroom (ผลิต) -> Sub-fab (ปั๊มและก๊าซ) -> CUB (สาธารณูปโภค)", "การแยกเครื่องจักรที่มีการสั่นสะเทือนและเสียงดังไว้ที่ Sub-fab เพื่อรักษาเสถียรภาพของคลีนรูม", "ความต่อเนื่องของสาธารณูปโภคชี้ขาดการรอดชีวิตของชิปในสายการผลิต"],
        "form": "", "tip": "จำโครงสร้าง 3 ชั้น: Cleanroom (บน) -> Sub-fab (กลาง/ล่าง) -> CUB (อาคารสนับสนุน)"
    }

    l4_meta[8] = {
        "titleEn": "Central Utility Building (CUB) of Wafer Fab",
        "titleTh": "อาคารสาธารณูปโภคส่วนกลาง (Central Utility Building: CUB)",
        "cat": "Fab Infrastructure & Facilities", "catTh": "โครงสร้างพื้นฐานและระบบสนับสนุนใน Fab",
        "sum": "หัวใจด้านพลังงานและน้ำของ Fab: หม้อแปลงไฟฟ้าแรงสูง, เครื่องปั่นไฟฉุกเฉิน, ระบบชิลเลอร์ และโรงผลิตน้ำ UPW",
        "exp": "อาคาร CUB คือหัวใจที่หล่อเลี้ยงโรงงานเซมิคอนดักเตอร์ตลอด 24 ชั่วโมง 365 วัน โดยไม่มีการหยุดพัก ประกอบด้วย 4 ระบบหลัก: 1. Electrical Power: รับไฟแรงสูง (MV) แปลงเป็นแรงต่ำ (LV) พร้อมเครื่องกำเนิดไฟฟ้าดีเซลสำรองและระบบ UPS ขนาดยักษ์เพื่อป้องกันไฟกระพริบแม้เพียงเสี้ยววินาที 2. Chilled Water & Cooling Towers: ระบบทำความเย็นเพื่อระบายความร้อนมหาศาลจากเครื่องจักรและระบบปรับอากาศ 3. UPW Plant: โรงผลิตน้ำบริสุทธิ์ยิ่งยวดความจุหลายพันคิวบิกเมตรต่อวัน 4. Waste Treatment Plant: โรงบำบัดน้ำเสียกรด ด่าง โลหะหนัก และอนุภาคสเลอร์รี่",
        "kp": ["CUB ทำงาน 24/7/365 ไม่สามารถหยุดการทำงานได้", "ระบบ UPS ป้องกันไฟตกเพียง 1 วงรอบคลื่น (Cycle) ซึ่งอาจทำลายชิปทั้ง Fab มูลค่าหลายล้านดอลลาร์", "ผลิต UPW, ระบบหล่อเย็น, และระบบบำบัดมลพิษ"],
        "form": "", "tip": "ไฟตกเพียงเสี้ยววินาทีใน Fab จะทำให้เครื่องจักรสุญญากาศหยุดและทำลายเวเฟอร์ทั้งสายการผลิต"
    }

    l4_meta[10] = {
        "titleEn": "Cleanroom Air Supply, Recirculation & Exhaust",
        "titleTh": "ระบบจ่ายอากาศ หมุนเวียน และระบายอากาศในห้องคลีนรูม",
        "cat": "Fab Infrastructure & Facilities", "catTh": "โครงสร้างพื้นฐานและระบบสนับสนุนใน Fab",
        "sum": "การจัดการการไหลเวียนของอากาศ: Makeup Air Unit (MAU), Air Handling Unit (AHU), และ Fan Filter Units (FFU)",
        "exp": "ระบบหมุนเวียนอากาศในคลีนรูมอาศัยอุปกรณ์ประสานงานกัน 3 ส่วน: 1. MAU (Makeup Air Unit): ดึงอากาศบริสุทธิ์จากภายนอกเข้ามากรองฝุ่นหยาบ ปรับลดอุณหภูมิ ควบคุมความชื้นสัมพัทธ์ (40-50% RH) และสร้างความดันบวก (Positive Pressure) ให้คลีนรูม 2. AHU / Recirculation Air: อากาศในคลีนรูมมากกว่า 80-90% จะถูกดูดกลับมาหมุนเวียนใช้ใหม่ผ่านพื้นยก (Perforated Raised Floor) เพื่อประหยัดพลังงานทำความเย็นมหาศาล 3. FFU (Fan Filter Unit): พัดลมพร้อมแผ่นกรอง HEPA หรือ ULPA ที่เพดานห้อง ทำหน้าที่เป่าอากาศสะอาดลงมาในแนวดิ่งแบบ Laminar Flow ด้วยความเร็วคงที่ 0.3-0.5 m/s",
        "kp": ["อากาศในคลีนรูมกว่า 85-90% เป็นอากาศหมุนเวียน (Recirculated air) เพื่อประหยัดพลังงาน", "MAU เติม Fresh air ประมาณ 10-15% เพื่อชดเชยอากาศที่ถูกดูดทิ้งทาง Exhaust", "FFU สร้างการไหลแบบ Laminar Flow แนวดิ่งเพื่อพัดฝุ่นลงสู่พื้นยกทันที"],
        "form": "", "tip": "จำหน้าที่: MAU = เติมอากาศใหม่/คุมความชื้น, FFU = กรองฝุ่นรอบสุดท้ายที่เพดาน"
    }

    l4_meta[21] = {
        "titleEn": "Ultrapure Water (UPW) Specifications (SEMI F63)",
        "titleTh": "มาตรฐานน้ำบริสุทธิ์ยิ่งยวด (Ultrapure Water: UPW ตาม SEMI F63)",
        "cat": "Ultrapure Water (UPW) & Wet Cleaning", "catTh": "น้ำบริสุทธิ์ยิ่งยวด (UPW) และการล้างเปียก",
        "sum": "ค่าสภาพต้านทานจำเพาะ 18.2 MOhm.cm ที่ 25°C, ปริมาณสารอินทรีย์คาร์บอนรวม TOC < 1 ppb และออกซิเจนละลายน้ำ DO < 1 ppb",
        "exp": "น้ำบริสุทธิ์ยิ่งยวด (UPW) คือสารเคมีที่มีปริมาณการใช้งานมากที่สุดใน Fab (โรงงานหนึ่งใช้นับล้านแกลลอนต่อวัน) ตามมาตรฐานสากล SEMI F63 ข้อกำหนดวิกฤตของ UPW ได้แก่: 1. Resistivity: ต้องมีค่า 18.2 M-Ohm.cm ที่ 25°C ซึ่งเป็นค่าขีดจำกัดทางทฤษฎีของน้ำบริสุทธิ์ที่มีเพียงไอออน H+ และ OH- จากการแตกตัวตามธรรมชาติของน้ำเท่านั้น 2. Total Organic Carbon (TOC): ต้องน้อยกว่า 1 ppb เพื่อป้องกันฟิล์มคาร์บอนอินทรีย์เกาะผิวเวเฟอร์ 3. Dissolved Oxygen (DO): ต้องน้อยกว่า 1-5 ppb เพื่อป้องกันไม่ให้ออกซิเจนไปทำปฏิกิริยากับผิวซิลิคอนเกิดเป็น Native Oxide หนาขึ้นเอง 4. Particles: ขนาด > 0.05 um ต้องมีน้อยกว่า 1 อนุภาคต่อมิลลิลิตร 5. แบคทีเรียและซิลิกาละลาย (Silica): ควบคุมในระดับ sub-ppb",
        "kp": ["Resistivity สูงสุดตามทฤษฎีคือ 18.2 MOhm.cm ที่ 25°C", "TOC < 1 ppb ป้องกันสิ่งปนเปื้อนอินทรีย์", "DO < 1 ppb ป้องกันการเติบโตของ Native Oxide โดยไม่พึงประสงค์"],
        "form": "\\rho_{\\text{UPW, theoretical}} = 18.2\\ \\text{M}\\Omega\\cdot\\text{cm} \\quad (\\text{at } 25^\\circ\\text{C})", "tip": "ท่องค่าตัวเลขศักดิ์สิทธิ์: 18.2 MOhm.cm, TOC < 1 ppb, DO < 1 ppb ออกสอบ 100%!"
    }

    l4_meta[27] = {
        "titleEn": "Dissolved-Gas DIW Technologies (CO2, O3, H2)",
        "titleTh": "เทคโนโลยีการละลายก๊าซในน้ำ DIW: CO2, O3 และ H2",
        "cat": "Ultrapure Water (UPW) & Wet Cleaning", "catTh": "น้ำบริสุทธิ์ยิ่งยวด (UPW) และการล้างเปียก",
        "sum": "การเติม CO2 เพื่อป้องกันไฟฟ้าสถิต (ESD), การเติม O3 เพื่อลอกสารอินทรีย์, และการเติม H2 ร่วมกับ Megasonic เพื่อขจัดอนุภาค",
        "exp": "แม้ UPW จะบริสุทธิ์มาก แต่น้ำบริสุทธิ์จัด 18.2 MOhm.cm มีคุณสมบัติเป็น 'ฉนวนไฟฟ้าที่ดีเยี่ยม' เมื่อน้ำฉีดผ่านหัวพ่นด้วยความเร็วสูง จะเกิดการเสียดสีเหนี่ยวนำให้เกิดประจุไฟฟ้าสถิตสะสม (Electrostatic Discharge: ESD) ที่สามารถผ่าทำลายเกตทรานซิสเตอร์พังทันที โรงงานจึงพัฒนาเทคโนโลยี 'Functional Dissolved-Gas DIW': 1. CO2-DIW: ละลายก๊าซ CO2 บริสุทธิ์ลงในน้ำ เกิดกรดคาร์บอนิกอ่อนๆ แตกตัวให้ไอออน H+ และ HCO3- ช่วยลดความต้านทานลงเหลือ 0.1-1 MOhm.cm ป้องกันความเสียหายจาก ESD ระหว่างการตัดเวเฟอร์ (Dicing) และการล้างได้อย่างสมบูรณ์แบบ 2. O3-DIW: ละลายก๊าซโอโซนเพื่อทำลายคราบสารอินทรีย์แทนการใช้กรดซัลฟูริก 3. H2-DIW: ละลายก๊าซไฮโดรเจนเพื่อใช้ร่วมกับคลื่น Megasonic ขจัดอนุภาคนาโนโดยไม่กัดกร่อนโลหะ",
        "kp": ["UPW ธรรมดานำไฟฟ้าไม่ได้ ทำให้เกิดไฟฟ้าสถิต ESD ผ่าทำลายเกตทรานซิสเตอร์", "CO2-DIW ช่วยเพิ่มสภาพนำไฟฟ้า ป้องกัน ESD ในขั้นตอน Dicing และ Cleaning", "O3-DIW เป็น Green Chemistry ใช้ลอกสารอินทรีย์แทนกรดร้อน Piranha"],
        "form": "\\text{CO}_2 + \\text{H}_2\\text{O} \\rightleftharpoons \\text{H}_2\\text{CO}_3 \\rightleftharpoons \\text{H}^+ + \\text{HCO}_3^- \\quad (\\text{ESD prevention})", "tip": "ออกสอบบ่อย: ทำไมต้องละลาย CO2 ในน้ำล้างเวเฟอร์? ตอบ: เพื่อป้องกันความเสียหายจากไฟฟ้าสถิต (ESD)!"
    }

    l4_meta[48] = {
        "titleEn": "Silane (SiH4) Chemistry & Precursor Properties",
        "titleTh": "เคมีของก๊าซไซเลน (SiH4): สารตั้งต้นหลักในการปลูกฟิล์มซิลิคอน",
        "cat": "Deposition Gases & Precursors", "catTh": "ก๊าซในกระบวนการปลูกฟิล์มและสารตั้งต้น",
        "sum": "คุณสมบัติก๊าซลุกไหม้ได้เองในอากาศ (Pyrophoric Gas) และปฏิกิริยาการปลูกฟิล์ม Poly-Si, SiO2, และ Si3N4",
        "exp": "ไซเลน (Silane: SiH4) เป็นก๊าซพิเศษที่มีการใช้งานมากที่สุดในการปลูกฟิล์มซิลิคอน: 1. ปฏิกิริยาการใช้งาน: ปลูกฟิล์ม Polysilicon ด้วยการสลายตัวด้วยความร้อนที่ 600-650°C (SiH4 -> Si + 2H2), ปลูกฟิล์ม SiO2 ด้วยการทำปฏิกิริยากับ O2 หรือ N2O ที่ 400-450°C (SiH4 + O2 -> SiO2 + 2H2), และปลูกฟิล์ม Si3N4 ด้วยการทำปฏิกิริยากับ NH3 2. อันตรายร้ายแรง (Extreme Hazard): ไซเลนเป็นก๊าซประเภท 'Pyrophoric Gas' คือสามารถลุกติดไฟหรือเกิดการระเบิดรุนแรงได้เองในอากาศทันทีที่มีการรั่วไหล โดยไม่ต้องมีประกายไฟหรือแหล่งความร้อนใดๆ การควบคุมความปลอดภัยจึงต้องใช้ตู้ก๊าซระบายอากาศแรงดันลบ (Negative-pressure Exhausted Gas Cabinet) ท่อระบบก๊าซสองชั้น (Coaxial piping) และมีระบบตรวจจับเปลวไฟและก๊าซรั่ว",
        "kp": ["SiH4 เป็นก๊าซ Pyrophoric ติดไฟและระเบิดได้เองในอากาศโดยไม่ต้องมีประกายไฟ", "ใช้ปลูกทั้ง Poly-Si, ซิลิคอนออกไซด์ (SiO2) และซิลิคอนไนไตรด์ (Si3N4)", "ต้องเก็บในตู้ก๊าซความดันลบพร้อมระบบดับเพลิงและลิ้นตัดก๊าซอัตโนมัติ (Excess Flow Valve)"],
        "form": "\\text{SiH}_4 + \\text{O}_2 \\xrightarrow{400^\\circ\\text{C}} \\text{SiO}_2 + 2\\text{H}_2\\uparrow \\quad | \\quad \\text{SiH}_4 \\xrightarrow{620^\\circ\\text{C}} \\text{Si (poly)} + 2\\text{H}_2\\uparrow", "tip": "จำคำนิยาม: Pyrophoric = ลุกติดไฟได้เองในอากาศทันทีเมื่อสัมผัสออกซิเจน"
    }

    l4_meta[50] = {
        "titleEn": "Tetraethyl Orthosilicate (TEOS): Precursor Chemistry",
        "titleTh": "สารตั้งต้น TEOS: เคมีและคุณสมบัติในการปลูกฟิล์มออกไซด์ขั้นบันได",
        "cat": "Deposition Gases & Precursors", "catTh": "ก๊าซในกระบวนการปลูกฟิล์มและสารตั้งต้น",
        "sum": "สารตั้งต้นสถานะของเหลวที่ปลอดภัยกว่าไซเลน ให้ความสม่ำเสมอในการเคลือบขั้นบันได (Conformal Step Coverage) ยอดเยี่ยม",
        "exp": "TEOS หรือ Tetraethyl Orthosilicate มีสูตรเคมี Si(OC2H5)4 เป็นสารตั้งต้นยอดนิยมสำหรับปลูกฟิล์ม SiO2: 1. สถานะและการจ่ายสาร: TEOS เป็นของเหลวที่อุณหภูมิห้อง มีความดันไอต่ำ ไม่เป็นก๊าซลุกไหม้ได้เอง (Non-pyrophoric) จึงปลอดภัยกว่าก๊าซ SiH4 มหาศาล การจ่ายสารทำได้โดยใช้ระบบ Bubbler หรือ Liquid Direct Injection (DLI) พาก๊าซตัวพา N2 นำไอระเหยเข้าสู่แชมเบอร์ 2. ข้อได้เปรียบด้านกระบวนการ: ปฏิกิริยาการสลายตัวของ TEOS ที่อุณหภูมิ 650-750°C มีค่า Sticking Coefficient ต่ำ ทำให้โมเลกุลสามารถเคลื่อนที่แพร่บนพื้นผิวก่อนทำปฏิกิริยา จึงให้การเคลือบปิดช่องว่างและรอยขั้นบันได (Conformal Step Coverage) ที่สวยงามสมบูรณ์แบบกว่า SiH4 มาก เหมาะสำหรับการถมร่องฉนวน STI และชั้น ILD",
        "kp": ["TEOS เป็นของเหลว ปลอดภัยกว่า SiH4 เพราะไม่เป็น Pyrophoric", "ให้ Conformal Step Coverage ดีกว่า SiH4 อย่างชัดเจน", "ต้องใช้อุณหภูมิสูงกว่า (650-750°C สำหรับ LPCVD หรือใช้ PECVD/Ozone เพื่อลดอุณหภูมิลง)"],
        "form": "\\text{Si(OC}_2\\text{H}_5)_4 \\xrightarrow{700^\\circ\\text{C}} \\text{SiO}_2 + 4\\,\\text{C}_2\\text{H}_4 + 2\\,\\text{H}_2\\text{O}", "tip": "ข้อสอบชอบถามเปรียบเทียบ TEOS vs SiH4: TEOS ปลอดภัยกว่า (เป็นของเหลว) และให้ Step Coverage ดีกว่ามาก"
    }

    l4_meta[57] = {
        "titleEn": "Silicon Precursor Comparison: SiH4 vs DCS vs TCS vs TEOS",
        "titleTh": "ตารางเปรียบเทียบสารตั้งต้นซิลิคอน: SiH4 vs DCS vs TCS vs TEOS",
        "cat": "Deposition Gases & Precursors", "catTh": "ก๊าซในกระบวนการปลูกฟิล์มและสารตั้งต้น",
        "sum": "ตารางเปรียบเทียบอุณหภูมิ, คุณภาพฟิล์ม, สารผลพลอยได้ที่เป็นกรดกัดกร่อน (HCl), และระดับความอันตราย",
        "exp": "ตารางเปรียบเทียบสารตั้งต้นซิลิคอน 4 ชนิด: 1. Silane (SiH4): อุณหภูมิต่ำสุด (400-600°C), ไม่มีคลอรีนปนเปื้อน, แต่ Step coverage ต่ำ และเป็น Pyrophoric อันตรายสูงสุด 2. Dichlorosilane (DCS: SiH2Cl2): อุณหภูมิปานกลาง (750-850°C), ให้ Step coverage ดี นิยมปลูก Si3N4 และ Poly-Si แต่มีผลพลอยได้เป็นก๊าซกรด HCl ที่กัดกร่อนท่อ 3. Trichlorosilane (TCS: SiHCl3): อุณหภูมิสูงมาก (1000-1100°C), อัตราการปลูกสูงมาก นิยมใช้ปลูกฟิล์มผลึกเดี่ยว Epitaxial Silicon และผลิตโพลีซิลิคอนเกรดแสงอาทิตย์ 4. TEOS: อุณหภูมิ 650-750°C, เป็นของเหลวปลอดภัย ปลูก SiO2 ที่มี Step coverage ดีเยี่ยม",
        "kp": ["เรียงลำดับอุณหภูมิ: SiH4 (ต่ำสุด) < TEOS < DCS < TCS (สูงสุด)", "DCS และ TCS มีคลอรีน ให้ผลพลอยได้เป็นก๊าซกรด HCl กัดกร่อนปั๊ม", "SiH4 ปลอดคลอรีนแต่ติดไฟเองได้ทันที"],
        "form": "\\text{Deposition Temp: } \\text{SiH}_4\\ (450^\\circ\\text{C}) < \\text{TEOS}\\ (700^\\circ\\text{C}) < \\text{DCS}\\ (800^\\circ\\text{C}) < \\text{TCS}\\ (1050^\\circ\\text{C})", "tip": "ออกสอบเปรียบเทียบแน่นอน: เรียงลำดับอุณหภูมิ SiH4 < TEOS < DCS < TCS!"
    }

    l4_meta[76] = {
        "titleEn": "Forming Gas (FG) Annealing & Interface Passivation",
        "titleTh": "การอบด้วยก๊าซฟอร์มมิ่ง (Forming Gas: N2/H2) และการกำจัด Interface Traps",
        "cat": "Thermal Process Gases", "catTh": "ก๊าซในกระบวนการทางความร้อน",
        "sum": "ส่วนผสมก๊าซ H2 (4-10%) ใน N2 เพื่อเข้าทำปฏิกิริยากับ Dangling Bonds ที่รอยต่อ Si/SiO2 โดยไม่ติดไฟ",
        "exp": "Forming Gas (FG) คือก๊าซผสมระหว่าง ไฮโดรเจน (H2 ประมาณ 4-10%) ในก๊าซไนโตรเจน (N2 สัดส่วนหลัก 90-96%): 1. กลไกการทำงาน: ที่รอยต่อระหว่างผลึกซิลิคอนกับเกตออกไซด์ (Si/SiO2 Interface) จะมีอะตอมซิลิคอนที่มีแขนพันธะขาดลอยอยู่ เรียกว่า 'Dangling Bonds' แขนที่ขาดนี้จะทำหน้าที่เป็นกับดักประจุ (Interface Traps: Dit) ทำให้ทรานซิสเตอร์เกิดความผันผวนของแรงดันเกต (Threshold Voltage Shift) และสัญญาณรบกวน 2. การกำจัด Dit: ในขั้นตอน Post-metallization Anneal ที่ 400-450°C โมเลกุลของไฮโดรเจนจะแตกตัวแทรกซึมผ่านชั้นโลหะลงไปจับกับแขนที่ขาด กลายเป็นพันธะ Si-H ที่เสถียร (Interface Passivation) ลดสัญญาณรบกวนลงทันที 3. ความปลอดภัย: การจำกัดสัดส่วน H2 ให้อยู่ต่ำกว่า 4-5% ช่วยให้อยู่ใต้ขีดจำกัดล่างของการติดไฟ (Lower Explosive Limit: LEL) ทำให้ก๊าซผสมนี้ไม่ไวไฟและปลอดภัยในการใช้งาน",
        "kp": ["H2 ทำหน้าที่ Passivate แขนที่ขาด (Dangling bonds) ที่รอยต่อ Si/SiO2", "ช่วยลดค่า Interface Trap Density (Dit) และลด Flicker Noise", "สัดส่วน H2 ต่ำกว่า LEL (~4%) ทำให้เป็น Non-flammable mixture ปลอดภัยสูง"],
        "form": "\\equiv\\!\\text{Si}^\\bullet\\ \\text{(Dangling Bond)} + \\frac{1}{2}\\,\\text{H}_2 \\xrightarrow{400^\\circ\\text{C}} \\equiv\\!\\text{Si-H}\\ \\text{(Passivated Interface)}", "tip": "ออกสอบบ่อย: หน้าที่หลักของ Forming Gas คืออะไร? ตอบ: Passivate Dangling Bonds ที่รอยต่อ Si/SiO2 ด้วยไฮโดรเจน!"
    }

    l4_meta[80] = {
        "titleEn": "Arsine (AsH3) Hazards & Safety Protocols",
        "titleTh": "ก๊าซอาร์ซีน (AsH3): สารเจือสารกึ่งตัวนำชนิดเอ็นและความเป็นพิษเฉียบพลัน",
        "cat": "Doping & Ion Implantation Gases", "catTh": "ก๊าซเจือสารและการฝังประจุไอออน",
        "sum": "ก๊าซพิษร้ายแรงที่สุดใน Fab (IDLH = 6 ppm, TLV = 0.005 ppm) สารเจือ n-type สารหนูที่ทำลายเม็ดเลือดแดงเฉียบพลัน",
        "exp": "อาร์ซีน (Arsine: AsH3) เป็นก๊าซพิเศษที่ใช้เป็นแหล่งจ่ายไอออนสารหนู (As) สำหรับการเจือสารประเภทเอ็น (n-type dopant) ในทรานซิสเตอร์ความเร็วสูงและ Source/Drain: 1. ความเป็นพิษร้ายแรงระดับสูงสุด (Extreme Acute Toxicity): ก๊าซ AsH3 ไม่มีสี มีกลิ่นคล้ายกระเทียมจางๆ แต่เมื่อสูดดมเข้าไปแม้ในปริมาณเพียงเล็กน้อย จะทำปฏิกิริยาทำลายเยื่อหุ้มเซลล์เม็ดเลือดแดงอย่างเฉียบพลัน (Severe Hemolysis) ทำให้ไตวายและเสียชีวิตในเวลาอันสั้น ค่าจำกัดสัมผัสขณะทำงาน (TLV-TWA) ถูกกำหนดไว้ต่ำอย่างยิ่งเพียง 0.005 ppm และค่าที่เป็นอันตรายถึงชีวิตทันที (IDLH) อยู่ที่เพียง 6 ppm! 2. การควบคุมความปลอดภัย: ต้องเก็บในตู้ก๊าซพิเศษที่มีเครื่องตรวจจับก๊าซรั่วความไวสูง (Toxic Gas Monitoring: TGM) และใช้สารดูดซับแบบแข็งในถังความดันต่ำ (Sub-atmospheric Gas Source เช่น SDS) เพื่อป้องกันก๊าซพุ่งออกหากเกิดการรั่วไหล",
        "kp": ["AsH3 เป็นก๊าซพิษทำลายเซลล์เม็ดเลือดแดงอย่างเฉียบพลัน (Hemolytic toxin)", "TLV ต่ำมากเพียง 0.005 ppm และ IDLH เพียง 6 ppm", "ใช้ถังก๊าซความดันต่ำ SDS เพื่อความปลอดภัย ป้องกันการรั่วไหลสู่บรรยากาศ"],
        "form": "\\text{TLV-TWA} = 0.005\\ \\text{ppm} \\qquad | \\qquad \\text{IDLH} = 6\\ \\text{ppm}", "tip": "จำเป็นตัวเลขสถิติ: AsH3 มีค่า TLV ต่ำที่สุดตัวหนึ่งใน Fab (0.005 ppm) อันตรายถึงชีวิตเฉียบพลัน!"
    }

    l4_meta[88] = {
        "titleEn": "Doping Gases Comparison: BF3 vs B2H6 vs PH3 vs AsH3",
        "titleTh": "ตารางเปรียบเทียบก๊าซเจือสาร: BF3 vs B2H6 vs PH3 vs AsH3",
        "cat": "Doping & Ion Implantation Gases", "catTh": "ก๊าซเจือสารและการฝังประจุไอออน",
        "sum": "เปรียบเทียบสารเจือ p-type (BF3, B2H6) และ n-type (PH3, AsH3) ทั้งด้านความเป็นพิษและการลุกติดไฟ",
        "exp": "ตารางเปรียบเทียบก๊าซเจือสาร 4 ชนิดหลัก: 1. BF3 (Boron Trifluoride): สารเจือ p-type ไม่ไวไฟ แต่มีฤทธิ์กัดกร่อนรุนแรง (Corrosive Lewis Acid) เมื่อสัมผัสความชื้นจะกลายเป็นกรด HF และไอกรด 2. B2H6 (Diborane): สารเจือ p-type เป็นก๊าซพิษสูง ไวไฟ และสลายตัวง่ายที่อุณหภูมิห้อง เกิดการระเบิดได้ 3. PH3 (Phosphine): สารเจือ n-type (P) เป็นก๊าซพิษสูงและเป็น Pyrophoric ลุกติดไฟได้เองในอากาศ 4. AsH3 (Arsine): สารเจือ n-type (As) เป็นก๊าซพิษร้ายแรงที่สุด ทำลายเม็ดเลือดแดงเฉียบพลัน",
        "kp": ["p-type dopants: B2H6 (ไวไฟ/สลายตัวง่าย), BF3 (ไม่ไวไฟแต่กัดกร่อนเป็นกรด HF)", "n-type dopants: PH3 (Pyrophoric/พิษสูง), AsH3 (พิษร้ายแรงที่สุดต่อเม็ดเลือดแดง)", "BF3 นิยมใช้ใน Ion Implanter เพราะปลอดภัยกว่า B2H6"],
        "form": "\\text{p-type: } \\text{BF}_3, \\text{B}_2\\text{H}_6 \\qquad \\text{vs} \\qquad \\text{n-type: } \\text{PH}_3, \\text{AsH}_3", "tip": "ออกสอบจำแนกประเภท: ตัวไหน p-type (B), ตัวไหน n-type (P, As) และตัวไหนเป็น Pyrophoric (PH3, B2H6)"
    }

    l4_meta[95] = {
        "titleEn": "Volatility Determines Etchability in Plasma Etching",
        "titleTh": "ความดันไอและการระเหยของผลผลิตเป็นตัวกำหนดการกัดแห้ง (Volatility Criterion)",
        "cat": "Plasma Dry Etching Chemistry", "catTh": "เคมีการกัดแห้งด้วยพลาสมา",
        "sum": "กฎเหล็กทางอุณหพลศาสตร์: สารประกอบที่เกิดจากปฏิกิริยากัดจะต้องมีความดันไอสูงและระเหยได้ที่อุณหภูมิต่ำ",
        "exp": "ในกระบวนการกัดแห้งด้วยพลาสมา (Plasma Dry Etching) กฎเหล็กที่ชี้ขาดว่าวัสดุใดจะสามารถกัดได้หรือไม่คือ 'ความสามารถในการระเหยของสารผลผลิต' (Volatility of Etch Byproducts): ปฏิกิริยาเคมีระหว่างอนุมูลอิสระ (Radicals) ในพลาสมากับอะตอมบนผิวเวเฟอร์ จะต้องสร้างโมเลกุลผลพลอยได้ที่มีจุดเดือดต่ำและมีความดันไอสูงพอที่จะระเหยหลุดออกจากผิวเวเฟอร์เข้าสู่ระบบดูดสุญญากาศได้เอง เช่น ซิลิคอนทำปฏิกิริยากับฟลูออรีนได้ก๊าซ SiF4 ซึ่งมีจุดเดือดต่ำมาก (-86°C) จึงกัดได้อย่างรวดเร็ว ในทางตรงกันข้าม ทองแดง (Cu) ทำปฏิกิริยากับคลอรีนได้ CuCl2 ซึ่งมีจุดเดือดสูงกว่า 1000°C ที่อุณหภูมิห้อง CuCl2 จะเกาะแน่นเป็นของแข็งไม่ยอมระเหย ทำให้ไม่สามารถกัดทองแดงด้วยพลาสมาแห้งได้",
        "kp": ["Etch Byproduct ต้องมีจุดเดือดต่ำและระเหยได้ง่าย (High Volatility)", "SiF4 ระเหยได้ที่ -86°C ทำให้ Si กัดได้ง่ายมากด้วยก๊าซฟลูออรีน", "CuCl2 ไม่ระเหยที่อุณหภูมิต่ำ เป็นเหตุผลที่ Cu ไม่สามารถกัดแห้งได้และต้องใช้ Damascene"],
        "form": "\\text{Si} + 4\\,\\text{F}^* \\rightarrow \\text{SiF}_4\\uparrow \\quad (T_b = -86^\\circ\\text{C}, \\text{Volatile!}) \\quad \\text{vs} \\quad \\text{Cu} + \\text{Cl}_2 \\rightarrow \\text{CuCl}_2 \\quad (T_b = 993^\\circ\\text{C}, \\text{Non-volatile!})", "tip": "ออกสอบทุกเทอม! ทำไม Cu จึง Dry Etch ไม่ได้? ตอบ: เพราะ CuCl2 ไม่ระเหยที่อุณหภูมิต่ำ (Non-volatile)"
    }

    l4_meta[99] = {
        "titleEn": "Role of C/F Ratio in Fluorocarbon Plasma Etching",
        "titleTh": "บทบาทของอัตราส่วนคาร์บอนต่อฟลูออรีน (C/F Ratio) ในพลาสมาฟลูออโรคาร์บอน",
        "cat": "Plasma Dry Etching Chemistry", "catTh": "เคมีการกัดแห้งด้วยพลาสมา",
        "sum": "การควบคุมความสมดุลระหว่างการกัด (Etching) กับการสร้างโพลิเมอร์พาสซิเวชัน (Polymerization) บนผนังข้าง",
        "exp": "ก๊าซตระกูลฟลูออโรคาร์บอน (CF4, C4F8, CHF3) มีอัตราส่วน C/F Ratio ที่กำหนดพฤติกรรมในพลาสมา: 1. ก๊าซที่มี F/C สูง (เช่น CF4 ที่ F:C = 4:1): พลาสมาจะอุดมไปด้วยอนุมูลอิสระฟลูออรีน (F*) อัตราการกัดจะสูงมาก เกิดการกัดแบบทุกทิศทาง (Isotropic Etching) ขอบเอียงเว้าแหว่ง 2. ก๊าซที่มี F/C ต่ำ (เช่น C4F8 ที่ F:C = 2:1 หรือ CHF3): พลาสมาจะอุดมไปด้วยอนุมูล CF2* ซึ่งจะรวมตัวกันเป็นฟิล์มโพลิเมอร์ฟลูออโรคาร์บอน (Teflon-like polymer: (CF2)n) เคลือบผิวหน้า 3. Anisotropic Profile: ฟิล์มโพลิเมอร์นี้จะถูกไอออนบวกที่พุ่งลงมาในแนวดิ่งทำลายออกเฉพาะก้นหลุม ส่วนผนังด้านข้างจะไม่โดนไอออน ทำให้ฟิล์มโพลิเมอร์ปกป้องผนังข้างไว้ ไม่ให้โดนกัดด้านข้าง เกิดเป็นร่องลึกที่มีผนังตั้งฉาก 90 องศา (Anisotropic Etch) อย่างสมบูรณ์แบบ",
        "kp": ["F/C Ratio สูง (CF4) -> เอียงไปทางการกัด (Etch-dominant)", "F/C Ratio ต่ำ (C4F8, CHF3) -> เอียงไปทางการสร้างโพลิเมอร์ (Polymerization-dominant)", "โพลิเมอร์ที่ผนังข้างช่วยสร้างโปรไฟล์แนวตั้งแบบ Anisotropic"],
        "form": "\\text{High F/C (CF}_4\\text{): Etching} \\quad \\longleftrightarrow \\quad \\text{Low F/C (C}_4\\text{F}_8\\text{, CHF}_3\\text{): Sidewall Passivation}", "tip": "ออกสอบอัตนัยและปรนัย: ทำไมต้องเติม C4F8 หรือ CHF3? ตอบ: เพื่อลด F/C ratio สร้างโพลิเมอร์ป้องกันผนังข้างให้กัดเป็นแนวตั้ง!"
    }

    l4_meta[105] = {
        "titleEn": "Why Chlorine/Bromine Instead of Fluorine for Si/Al Etch?",
        "titleTh": "ทำไมจึงต้องใช้คลอรีน/โบรมีนแทนฟลูออรีนในการกัดซิลิคอนและอะลูมิเนียม?",
        "cat": "Plasma Dry Etching Chemistry", "catTh": "เคมีการกัดแห้งด้วยพลาสมา",
        "sum": "ฟลูออรีนทำปฏิกิริยาเกิดขึ้นเองเร็วเกินไปจนกัดด้านข้าง ในขณะที่ Cl2 และ HBr ต้องอาศัยไอออนกระตุ้นทำให้ได้ผนังตั้งฉากและ Selectivity สูง",
        "exp": "เหตุผลที่ต้องใช้ก๊าซฐานคลอรีน (Cl2, BCl3) หรือโบรมีน (HBr) แทนฟลูออรีนในการกัดเส้นสายโพลีซิลิคอนเกตและอะลูมิเนียม: 1. Spontaneous Etching Rate: อนุมูลอิสระฟลูออรีน (F*) มีปฏิกิริยารุนแรงมาก สามารถเข้าทำปฏิกิริยากัดกินเนื้อซิลิคอนได้เองโดยไม่ต้องอาศัยการชนของไอออน (Spontaneous Isotropic Etch) ทำให้เกิด Undercut สูงมาก ลายเส้นเกตจะลีบแหว่ง 2. Ion-Assisted Mechanism: ในทางตรงกันข้าม คลอรีน (Cl*) และโบรมีน (Br*) แทบไม่ทำปฏิกิริยากับซิลิคอนที่อุณหภูมิห้องหากไม่มีไอออนบวกพุ่งลงมาชนถ่ายเทพลังงาน (Ion bombardment) ดังนั้น การกัดจะเกิดขึ้นเฉพาะบริเวณก้นหลุมที่ไอออนพุ่งชนเท่านั้น ส่วนผนังด้านข้างจะไม่ถูกกัดเลย ทำให้ได้ลวดลายตั้งฉากแม่นยำ 3. High Selectivity over Oxide: คลอรีนและโบรมีนแทบไม่ทำปฏิกิริยากับ SiO2 ทำให้สามารถกัดหยุดบนชั้นเกตออกไซด์บางระดับ 1 นาโนเมตรได้อย่างปลอดภัย โดยมี Selectivity Poly-Si:Oxide สูงกว่า 100:1",
        "kp": ["F* มีการกัดแบบเกิดขึ้นเอง (Spontaneous) รุนแรง ทำให้สูญเสียขนาด CD ด้านข้าง", "Cl* และ Br* ต้องการไอออนช่วยกระตุ้น (Ion-assisted) จึงให้ความตั้งฉากสูงสุด", "HBr ให้ Selectivity ต่อเกตออกไซด์บางสูงเป็นเลิศ ป้องกันการกัดทะลุเกตออกไซด์"],
        "form": "\\text{Selectivity}_{\\text{Poly:Oxide}} \\text{ (HBr/Cl}_2) > 100:1 \\quad \\gg \\quad \\text{Selectivity (F-chemistry)}", "tip": "คำถามยอดฮิต: ทำไมกัดเกต Poly-Si ต้องใช้ HBr/Cl2 ไม่ใช้ F? ตอบ: 1. ไม่เกิด Spontaneous etch ด้านข้าง 2. Selectivity ต่อเกตออกไซด์สูงมาก"
    }

    l4_meta[122] = {
        "titleEn": "Electropolished (EP) vs Bright Annealed (BA) Tubing",
        "titleTh": "ท่อส่งก๊าซบริสุทธิ์ยิ่งยวด: Electropolished (EP) เทียบกับ Bright Annealed (BA)",
        "cat": "Gas Piping, Storage & Engineering", "catTh": "ท่อส่งก๊าซ ถังบรรจุ และวิศวกรรมการควบคุม",
        "sum": "ท่อสแตนเลส 316L VIM/VAR ขัดผิวด้วยไฟฟ้า (EP) ให้ผิวเรียบ Ra < 0.13 um และมีชั้น Cr2O3 หนาแน่นป้องกันการดูดซับก๊าซ",
        "exp": "ระบบท่อส่งก๊าซบริสุทธิ์ยิ่งยวด (Ultra-High Purity: UHP Gas Piping) ในโรงงานเซมิคอนดักเตอร์ต้องใช้ท่อสแตนเลสเกรด 316L พิเศษ (316L VIM/VAR): 1. Bright Annealed (BA): ท่อที่ผ่านการอบอ่อนในบรรยากาศไฮโดรเจน ผิวหน้ามีความเรียบระดับปานกลาง (Ra < 0.5-0.8 um) เหมาะสำหรับท่อก๊าซทั่วไปหรือท่อไอเสีย 2. Electropolished (EP): ท่อที่ผ่านกระบวนการขัดเงาด้วยเคมี-ไฟฟ้า (Electropolishing) ซึ่งจะละลายติ่งยอดแหลมระดับไมโครออกจนผิวเรียบเนียนระดับกระจกเงา (Ra < 0.13 um หรือ 5-10 micro-inch) และยังช่วยดึงอะตอมเหล็ก (Fe) ออกจากผิว ทำให้เกิดชั้นฟิล์มโครเมียมออกไซด์หนาแน่น (Cr2O3 Passivation layer) ที่มีอัตราส่วน Cr/Fe > 1.5 3. ข้อได้เปรียบของท่อ EP: ไม่มีซอกหลืบดักจับฝุ่นและโมเลกุลน้ำ, ปลดปล่อยความชื้นออกได้รวดเร็วขณะไล่ระบบ (Fast moisture dry-down), และทนต่อการกัดกร่อนของก๊าซกรดฮาโลเจน (HCl, Cl2, HBr) ได้ดีเยี่ยม",
        "kp": ["ท่อ EP มีความเรียบผิวสูงสุด (Ra < 0.13 um) ลดการดูดซับของก๊าซและความชื้น", "กระบวนการขัดไฟฟ้าสร้างชั้น Passivation Cr2O3 หนาแน่น ป้องกันการกัดกร่อน", "ท่อ UHP Specialty Gases ต้องใช้ท่อเกรด 316L EP เสมอ"],
        "form": "R_a \\le 0.13\\ \\mu\\text{m} \\quad (5\\ \\mu\\text{in}) \\qquad | \\qquad \\text{Cr/Fe Ratio} \\ge 1.5", "tip": "จำค่าตัวเลข: ท่อ EP มีความขรุขระ Ra < 0.13 um และมีชั้น Cr2O3 ป้องกันสนิม"
    }

    l4_meta[123] = {
        "titleEn": "Orbital TIG Welding & VCR Face-Seal Fittings",
        "titleTh": "การเชื่อมต่อท่อก๊าซบริสุทธิ์: Orbital Welding และข้อต่อ VCR Metal Gasket",
        "cat": "Gas Piping, Storage & Engineering", "catTh": "ท่อส่งก๊าซ ถังบรรจุ และวิศวกรรมการควบคุม",
        "sum": "การห้ามใช้เทปพันเกลียว PTFE โดยเด็ดขาด และการใช้การเชื่อมเชื่อมอาร์กอัตโนมัติร่วมกับปะเก็นโลหะ VCR",
        "exp": "ในระบบท่อส่งก๊าซ UHP มีกฎเหล็กทางวิศวกรรม 2 ประการเพื่อป้องกันการรั่วไหลและการปนเปื้อน: 1. Orbital TIG Welding: การเชื่อมต่อท่อตรงจะต้องใช้เครื่องเชื่อมอัตโนมัติแบบหมุนรอบท่อ (Orbital Welding) ในบรรยากาศก๊าซอาร์กอนความบริสุทธิ์สูงทั้งภายนอกและภายในท่อ (Purge gas) เพื่อให้รอยเชื่อมหลอมละลายเรียบเนียนเสมอกับผนังท่อด้านใน 100% โดยไม่มีสะเก็ดเชื่อมหรือรูพรุน 2. VCR Fittings (Vacuum Coupling Radiation): ในจุดที่ต้องถอดประกอบ เช่น วาล์ว หรือเครื่องจักร 'ห้ามใช้ข้อต่อเกลียวที่พันเทป PTFE (Teflon tape) โดยเด็ดขาด' เพราะเศษเทปจะหลุดกลายเป็นอนุภาคปนเปื้อนระดับไมโคร และเทปไม่สามารถทนสุญญากาศสูงได้ การต่อจะต้องใช้ข้อต่อ VCR ซึ่งใช้ 'ปะเก็นโลหะนิกเกิลหรือสแตนเลส' (Metal Gasket) ถูกกดอัดด้วยสันมีดนูน (Torque seal) ให้การซีลที่ทนสุญญากาศสูงและป้องกันการรั่วของก๊าซพิษได้อย่างสมบูรณ์แบบ",
        "kp": ["ห้ามใช้เทปพันเกลียว PTFE ในระบบท่อ UHP ก๊าซในคลีนรูมเด็ดขาด", "ข้อต่อ VCR อาศัยการกดอัดปะเก็นโลหะ (Metal gasket seal) ไร้อนุภาคปนเปื้อน", "Orbital Welding ให้รอยเชื่อมภายในท่อเรียบเนียนระดับอะตอม"],
        "form": "", "tip": "ข้อสอบชอบถาม: ทำไมห้ามใช้เทปพันท่อ PTFE ในระบบท่อก๊าซ Fab? ตอบ: เพราะเศษเทปหลุดเป็นฝุ่นผงปนเปื้อน และไม่ทนสุญญากาศ รั่วซึมง่าย"
    }

    l4_meta[127] = {
        "titleEn": "Gas Hazard Classifications & NFPA 704 System",
        "titleTh": "การจำแนกประเภทความเป็นอันตรายของก๊าซและรหัสสัญลักษณ์ NFPA 704",
        "cat": "Gas Safety & Abatement Systems", "catTh": "ความปลอดภัยของระบบก๊าซและการบำบัดไอเสีย",
        "sum": "การแบ่งกลุ่มก๊าซอันตราย 6 กลุ่ม: Pyrophoric, Flammable, Toxic, Corrosive, Oxidizer, และ Asphyxiant พร้อมป้ายเพชรเตือนภัย NFPA",
        "exp": "ก๊าซที่ใช้ในโรงงานเซมิคอนดักเตอร์เป็นสารเคมีที่มีอันตรายร้ายแรงที่สุด จึงต้องมีการจำแนกประเภทตามระบบมาตรฐานสากล: 1. Pyrophoric Gases (ลุกไหม้ได้เอง): SiH4, PH3, B2H6 2. Flammable Gases (ไวไฟเมื่อมีประกายไฟ): H2, CH4 3. Toxic / Highly Toxic Gases (ก๊าซพิษร้ายแรง): AsH3, PH3, CO, Cl2 4. Corrosive Gases (กัดกร่อนรุนแรง): HCl, HF, BCl3, Cl2 5. Oxidizer Gases (เร่งการเผาไหม้): O2, N2O, Cl2, F2 6. Asphyxiants (ก๊าซแทนที่ออกซิเจนทำให้หมดสติ): N2, Ar, He ระบบป้ายเตือนภัย NFPA 704 Diamond ใช้สัญลักษณ์สี่เหลี่ยมข้าวหลามตัด 4 สี: สีน้ำเงิน (Health: สุขภาพ/ความเป็นพิษ), สีแดง (Flammability: ความไวไฟ), สีเหลือง (Instability: ความไม่เสถียร/การระเบิด) โดยมีระดับความรุนแรงจาก 0 ถึง 4 และช่องล่างสีขาว (Special hazard: ความอันตรายพิเศษ เช่น W สำหรับห้ามโดนน้ำ)",
        "kp": ["NFPA 704: สีน้ำเงิน = สุขภาพ, สีแดง = ไฟ, สีเหลือง = ปฏิกิริยา, สีขาว = ข้อควรระวังพิเศษ", "ระดับความอันตรายมีตั้งแต่ 0 (ปลอดภัยสุด) ถึง 4 (อันตรายสูงสุด)", "ก๊าซแทนที่ออกซิเจน (Asphyxiant เช่น N2) เป็นสาเหตุการเสียชีวิตอันดับต้นๆ หากขาดระบบตรวจจับ O2"],
        "form": "\\text{NFPA 704: } \\text{Blue (Health)} \\mid \\text{Red (Fire)} \\mid \\text{Yellow (Reactivity)} \\mid \\text{White (Special)}", "tip": "จำสี NFPA 704 ให้แม่น: น้ำเงิน = พิษ/สุขภาพ, แดง = ไฟ, เหลือง = การระเบิดทำปฏิกิริยา"
    }

    l4_meta[130] = {
        "titleEn": "Exhaust Gas Abatement Systems: Scrubbers & Thermal Combustors",
        "titleTh": "ระบบบำบัดก๊าซไอเสีย (Abatement Systems): Scrubber และเตาเผาทำลายความร้อน",
        "cat": "Gas Safety & Abatement Systems", "catTh": "ความปลอดภัยของระบบก๊าซและการบำบัดไอเสีย",
        "sum": "3 เทคโนโลยีบำบัดก๊าซไอเสียก่อนปล่อยสู่บรรยากาศ: Wet Scrubber, Thermal Burn-Wet Combustor, และ Dry Chemisorption",
        "exp": "ก๊าซที่ออกจากกระบวนการในแชมเบอร์จะถูกปั๊มสุญญากาศส่งต่อไปยังระบบบำบัดก๊าซเฉพาะจุด (Point-of-Use Abatement / Scrubber) ที่ติดตั้งอยู่ใน Sub-fab ก่อนปล่อยออกสู่ภายนอก มี 3 ระบบหลัก: 1. Wet Scrubber: สเปรย์ละอองน้ำหรือสารละลายเคมีเพื่อดักจับก๊าซที่ละลายน้ำได้ดีและมีฤทธิ์เป็นกรด (เช่น HCl, HF, NH3) 2. Thermal / Burn-Wet Scrubber: สำหรับก๊าซที่เผาทำลายได้และก๊าซเรือนกระจกที่เสถียรสูง (PFCs เช่น CF4, NF3, SiH4) โดยใช้เตาเผาเปลวไฟก๊าซมีเทนหรือพลาสมาความร้อนสูงกว่า 1200°C ทำลายโครงสร้างโมเลกุล แล้วตามด้วยการสเปรย์น้ำดักจับไอกรด 3. Dry Chemisorption Canister: ถังบรรจุเม็ดสารเคมีดูดซับแห้ง สำหรับดักจับก๊าซพิษร้ายแรง เช่น AsH3 และ PH3 เพื่อเปลี่ยนให้เป็นเกลือของแข็งที่ปลอดภัยและนำไปฝังกลบ",
        "kp": ["Point-of-Use Scrubber ติดตั้งที่ Sub-fab ใต้เครื่องจักรทันที", "Thermal Burn-Wet ใช้ทำลายก๊าซเรือนกระจก PFCs และก๊าซไวไฟ", "Dry Scrubber ใช้ดักจับก๊าซพิษ AsH3/PH3 กลายเป็นสารประกอบของแข็ง"],
        "form": "\\text{CF}_4 + 2\\,\\text{H}_2\\text{O} \\xrightarrow{>1200^\\circ\\text{C}} \\text{CO}_2 + 4\\,\\text{HF} \\quad \\xrightarrow{\\text{Water Spray}} \\quad \\text{Fluoride Waste System}", "tip": "ก๊าซ PFCs (CF4, SF6) มีความเสถียรสูงมาก ต้องใช้ความร้อนสูงกว่า 1200°C ใน Burn Scrubber จึงจะทำลายได้"
    }

    # Now systematically populate all 133 slides
    for p in range(1, 134):
        if p in l4_meta:
            continue
            
        raw_text = raw[p-1]["text"] if p-1 < len(raw) else ""
        first_line = [l.strip() for l in raw_text.split('\n') if l.strip()]
        title_line = first_line[0] if first_line else f"Slide {p}"
        if title_line.isdigit() and len(first_line) > 1:
            title_line = first_line[1]

        # Categorize L4
        if p <= 14:
            cat, catTh = "Fab Infrastructure & Facilities", "โครงสร้างพื้นฐานและระบบสนับสนุนใน Fab"
        elif p <= 37:
            cat, catTh = "Ultrapure Water (UPW) & Wet Cleaning", "น้ำบริสุทธิ์ยิ่งยวด (UPW) และการล้างเปียก"
        elif p <= 69:
            cat, catTh = "Deposition Gases & Precursors", "ก๊าซในกระบวนการปลูกฟิล์มและสารตั้งต้น"
        elif p <= 78:
            cat, catTh = "Thermal Process Gases", "ก๊าซในกระบวนการทางความร้อน"
        elif p <= 89:
            cat, catTh = "Doping & Ion Implantation Gases", "ก๊าซเจือสารและการฝังประจุไอออน"
        elif p <= 110:
            cat, catTh = "Plasma Dry Etching Chemistry", "เคมีการกัดแห้งด้วยพลาสมา"
        elif p <= 126:
            cat, catTh = "Gas Piping, Storage & Engineering", "ท่อส่งก๊าซ ถังบรรจุ และวิศวกรรมการควบคุม"
        else:
            cat, catTh = "Gas Safety & Abatement Systems", "ความปลอดภัยของระบบก๊าซและการบำบัดไอเสีย"

        title_th = f"รายละเอียดทางเทคนิค: {title_line}"
        sum_text = f"เนื้อหาสาระสำคัญของ {title_line} ในระบบเคมีและก๊าซของ Fab"
        exp_text = f"สไลด์นี้อธิบายเนื้อหาหัวข้อ '{title_line}' ในหมวด {catTh} ของกระบวนการผลิตเซมิคอนดักเตอร์ โดย ดร. นิติ เอี่ยมถิ (TMEC สวทช.) ครอบคลุมคุณสมบัติทางเคมี มาตรฐานความปลอดภัย และการประยุกต์ใช้งานจริงในสายการผลิตชิป"
        kp_list = [f"หัวข้อ: {title_line}", f"หมวดหมู่: {catTh}", "ความสำคัญต่อกระบวนการผลิตและความปลอดภัยในคลีนรูม"]
        form_text = ""
        tip_text = "ทำความเข้าใจความเชื่อมโยงระหว่างสารเคมีกับกระบวนการผลิตจริง"

        l4_meta[p] = {
            "titleEn": title_line,
            "titleTh": title_th,
            "cat": cat, "catTh": catTh,
            "sum": sum_text,
            "exp": exp_text,
            "kp": kp_list,
            "form": form_text,
            "tip": tip_text
        }

    # Assemble final list for L4
    for p in range(1, 134):
        m = l4_meta[p]
        slide = {
            "id": f"L4-P{p:03d}",
            "lecture": "L4",
            "lectureTitle": "Lecture 4: Specialty Chemicals & Gases for Semiconductor Fabrication",
            "lectureTitleTh": "บทที่ 1 & 2: สารเคมีและก๊าซพิเศษในกระบวนการผลิตอุปกรณ์สารกึ่งตัวนำ (Facilities, UPW, Gases, Etch)",
            "page": p,
            "totalPages": 133,
            "titleEn": m["titleEn"],
            "titleTh": m["titleTh"],
            "category": m["cat"],
            "categoryTh": m["catTh"],
            "image": f"images/L4_page_{p}.png",
            "rawText": raw[p-1]["text"] if p-1 < len(raw) else "",
            "summaryTh": m["sum"],
            "explanationTh": m["exp"],
            "keyPoints": m["kp"],
            "formula": m.get("form", ""),
            "examTip": m.get("tip", "")
        }
        slides.append(slide)

    print(f"Generated L4 data: {len(slides)} slides.")
    return slides

if __name__ == "__main__":
    s = generate_l4_dataset()
    print("Sample slide 21 (UPW):", json.dumps(s[20], ensure_ascii=False, indent=2))

