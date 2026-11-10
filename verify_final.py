import json

with open('slides_data.js', 'r', encoding='utf-8') as f:
    slides = json.loads(f.read().split('window.ALL_SLIDES = ', 1)[1].rstrip(';\n'))

print(f"Total slides in database: {len(slides)}")

queries = ['Preston', 'UPW', 'TMAH', 'EUV', 'SiH4', 'Megasonic', 'CUB', 'BARC', 'Damascene']
for q in queries:
    matches = [s['id'] for s in slides if q.lower() in (s['titleEn'] + ' ' + s['explanationTh'] + ' ' + s['summaryTh']).lower()]
    print(f"Query '{q}': {len(matches)} matches -> {matches[:4]}")

# Sample slide check
sample = slides[23] # L4-P024 (UPW diagram)
print("\n--- SAMPLE SLIDE L4-P024 ---")
print("Title:", sample['titleEn'], "/", sample['titleTh'])
print("Formula:", sample['formula'])
print("Summary:", sample['summaryTh'])
print("Explanation preview:", sample['explanationTh'][:250].replace('\n', ' '))
print("Key points count:", len(sample['keyPoints']))
print("Exam tip preview:", sample['examTip'][:150])
