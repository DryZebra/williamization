import os
import re
import glob

def extract_rules():
    archive_dir = "conversations"
    md_files = glob.glob(os.path.join(archive_dir, "**", "*.md"), recursive=True)

    smoothing_phrases = [
        "that's a great question",
        "that's a fascinating perspective",
        "i completely agree with you",
        "it's worth noting",
        "as an ai",
        "hope this helps",
        "feel free to ask",
        "i'd be happy to help",
        "certainly!"
    ]

    william_structures = [
        "the functional machine",
        "dialectical motion",
        "shape of motion",
        "invariant collapse",
        "resonance",
        "materialist christianity"
    ]

    counts_smoothing = {p: 0 for p in smoothing_phrases}
    counts_william = {w: 0 for w in william_structures}

    for fpath in md_files:
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read().lower()

            for p in smoothing_phrases:
                if p in text:
                    counts_smoothing[p] += 1

            for w in william_structures:
                if w in text:
                    counts_william[w] += 1
        except Exception:
            pass

    print("=== DEEP ARCHIVE PATTERN EXTRACTION (2,352 FILES) ===")
    print("\n[TOP ASSISTANT SMOOTHING TROPES FOUND IN LOGS]:")
    for k, v in sorted(counts_smoothing.items(), key=lambda x: x[1], reverse=True):
        print(f"  - '{k}': {v} files")

    print("\n[TOP WILLIAM DIALECTICAL STRUCTURES FOUND IN LOGS]:")
    for k, v in sorted(counts_william.items(), key=lambda x: x[1], reverse=True):
        print(f"  - '{k}': {v} files")

if __name__ == "__main__":
    extract_rules()
