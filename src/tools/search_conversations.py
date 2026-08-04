import os
import re
from typing import List, Dict

CONV_DIR = r"C:\Users\ezrab\OneDrive - Durham Technical Community College\Desktop\OKF\conversations"

KEYWORDS = [
    "william",
    "williamization",
    "chamber of motion",
    "consciousness project",
    "re-uptake",
    "reuptake",
    "inverted mask"
]

def search_files():
    matches: Dict[str, List[str]] = {kw: [] for kw in KEYWORDS}
    file_count = 0

    for root, _, files in os.walk(CONV_DIR):
        for file in files:
            if file.endswith((".md", ".json", ".txt")):
                file_count += 1
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    content_lower = content.lower()
                    for kw in KEYWORDS:
                        if kw in content_lower:
                            # Extract short snippet
                            idx = content_lower.find(kw)
                            snippet = content[max(0, idx-100):min(len(content), idx+200)].replace("\n", " ")
                            matches[kw].append(f"{os.path.basename(full_path)}: ...{snippet}...")
                except Exception as e:
                    pass

    print(f"Scanned {file_count} files in conversation archive.\n")
    for kw, results in matches.items():
        print(f"=== Keyword: '{kw}' ({len(results)} matches) ===")
        for r in results[:5]:
            print(f"  - {r}")
        print()

if __name__ == "__main__":
    search_files()
