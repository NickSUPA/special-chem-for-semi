# -*- coding: utf-8 -*-
import json
import os
import time
import subprocess

LECTURES = [
    ("L4", 133),
    ("L5", 105),
    ("L6", 64)
]

def check_progress():
    total_slides = 302
    completed_slides = 0
    results = {}
    
    for code, total in LECTURES:
        fname = f"cache_{code.lower()}.json"
        if os.path.exists(fname):
            try:
                with open(fname, "r", encoding="utf-8") as f:
                    data = json.load(f)
                count = len(data)
                # check valid entries
                valid = sum(1 for v in data.values() if isinstance(v, dict) and len(v.get("explanationTh", "")) >= 80)
            except Exception:
                count = 0
                valid = 0
        else:
            count = 0
            valid = 0
            
        completed_slides += valid
        pct = (valid / total) * 100.0
        results[code] = {
            "total": total,
            "cached": count,
            "valid": valid,
            "pct": pct
        }
        
    overall_pct = (completed_slides / total_slides) * 100.0
    remaining = total_slides - completed_slides
    
    print("-" * 55)
    print(f"PROGRESS UPDATE [{time.strftime('%H:%M:%S')}]:")
    for code, info in results.items():
        bar_len = 20
        filled = int(bar_len * info['valid'] / info['total'])
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  {code}: [{bar}] {info['valid']:3d}/{info['total']:3d} ({info['pct']:5.1f}%)")
    
    overall_bar = int(25 * completed_slides / total_slides)
    bar_str = "█" * overall_bar + "░" * (25 - overall_bar)
    print(f"\n  OVERALL: [{bar_str}] {completed_slides}/{total_slides} ({overall_pct:.1f}%)")
    print(f"  REMAINING: {remaining} slides")
    print("-" * 55)
    return completed_slides, remaining

if __name__ == "__main__":
    check_progress()

