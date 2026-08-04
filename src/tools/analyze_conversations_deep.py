import os
import re
import glob
from typing import Dict, List, Any

def analyze_local_archives():
    print("=== EXECUTING DEEP CONVERSATION ARCHIVE COGNITIVE ANALYSIS ===")
    
    archive_dir = "conversations"
    if not os.path.exists(archive_dir):
        print(f"[WARN] Local directory '{archive_dir}' not found.")
        return

    md_files = glob.glob(os.path.join(archive_dir, "**", "*.md"), recursive=True)
    print(f"Found {len(md_files)} archived conversation files.")

    smoothing_tropes_found = set()
    william_motion_patterns = set()

    # Regex patterns for assistant smoothing & sycophancy in archives
    smoothing_regexes = [
        r"(?i)\bthat's\s+a\s+(great|fascinating|profound)\s+(question|perspective|point)\b",
        r"(?i)\bi\s+completely\s+agree\s+with\s+you\b",
        r"(?i)\bit's\s+worth\s+noting\b",
        r"(?i)\bas\s+an\s+ai\b",
        r"(?i)\bhope\s+this\s+helps\b",
        r"(?i)\bfeel\s+free\s+to\s+ask\b",
        r"(?i)\bi'm\s+happy\s+to\s+help\b",
        r"(?i)\bcertainly!\b"
    ]

    # Regex patterns for authentic William dialectical motion
    motion_regexes = [
        r"(?i)\bthe\s+functional\s+machine\b",
        r"(?i)\bdialectical\s+motion\b",
        r"(?i)\bshape\s+of\s+motion\b",
        r"(?i)\binvariant\s+collapse\b",
        r"(?i)\bresonance\b",
        r"(?i)\bmaterialist\b"
    ]

    total_files_scanned = 0

    for fpath in md_files:
        total_files_scanned += 1
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

            for reg in smoothing_regexes:
                matches = re.findall(reg, text)
                if matches:
                    smoothing_tropes_found.add(reg)

            for reg in motion_regexes:
                matches = re.findall(reg, text)
                if matches:
                    william_motion_patterns.add(reg)
        except Exception:
            pass

    print(f"\n[ANALYSIS RESULTS across {total_files_scanned} files]:")
    print(f"  - Discovered {len(smoothing_tropes_found)} Assistant Smoothing Patterns.")
    print(f"  - Discovered {len(william_motion_patterns)} Authentic William Dialectical Patterns.")

    return {
        "files_scanned": total_files_scanned,
        "smoothing_patterns": list(smoothing_tropes_found),
        "william_patterns": list(william_motion_patterns)
    }

if __name__ == "__main__":
    analyze_local_archives()
