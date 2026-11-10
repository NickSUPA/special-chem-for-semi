import os
import fitz # PyMuPDF
import time

pdfs = [
    ('L4_Specialty Chemicals and Gases for Semiconductor Devices Fabrication_V4_NA_01092026.pdf', 'L4', 133),
    ('L5_Specialty gases and chemicals for Lithography process_NA_V1_22092026.pdf', 'L5', 105),
    ('Lecture 6_CMP chemicals_NA_V1_13102026.pdf', 'L6', 64)
]

os.makedirs('images', exist_ok=True)
t0 = time.time()
extracted_count = 0

for pdf_path, prefix, total in pdfs:
    doc = fitz.open(pdf_path)
    for p_idx in range(len(doc)):
        page_num = p_idx + 1
        out_name = os.path.join('images', f'{prefix}_page_{page_num}.png')
        if not os.path.exists(out_name):
            page = doc[p_idx]
            pix = page.get_pixmap(dpi=150)
            pix.save(out_name)
            extracted_count += 1
            if extracted_count % 20 == 0:
                print(f"Extracted {extracted_count} images... (current: {out_name})")

print(f"Extraction complete! Newly extracted: {extracted_count} images in {time.time()-t0:.2f} seconds.")

