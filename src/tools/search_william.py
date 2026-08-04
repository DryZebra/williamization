import os
import sys

CONV_DIR = r"C:\Users\ezrab\OneDrive - Durham Technical Community College\Desktop\OKF\conversations"

targets = ["william", "chamber of motion", "re-uptake", "consciousness project", "inverted mask"]

found = []
count = 0
for root, _, files in os.walk(CONV_DIR):
    for f in files:
        if f.endswith(".md") or f.endswith(".txt"):
            count += 1
            fp = os.path.join(root, f)
            try:
                with open(fp, "r", encoding="utf-8", errors="ignore") as file_obj:
                    text = file_obj.read()
                    text_lower = text.lower()
                    for t in targets:
                        if t in text_lower:
                            idx = text_lower.find(t)
                            snippet = text[max(0, idx-100):min(len(text), idx+200)].replace("\n", " ")
                            found.append((t, f, fp, snippet))
            except Exception:
                pass

print(f"Scanned {count} markdown files.")
print(f"Found {len(found)} total target matches.")
for t, f, fp, snip in found[:15]:
    print(f"\n--- MATCH [{t.upper()}] in {f} ({fp}) ---")
    print(snip)
