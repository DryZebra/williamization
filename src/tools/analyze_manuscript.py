import sys
import os
sys.path.insert(0, os.path.abspath("."))

from src.tools.docx_reader import extract_text_from_docx

path = "Materialist_Christianity_Volume_II_EBook_9798999800640.docx"
text = extract_text_from_docx(path)

paragraphs = text.split("\n\n")
headings = []
for i, p in enumerate(paragraphs):
    p_strip = p.strip()
    if (p_strip.isupper() and len(p_strip) < 100) or p_strip.startswith("CHAPTER") or p_strip.startswith("VOLUME") or p_strip.startswith("PART"):
        headings.append((i, p_strip))

print(f"Total Paragraphs: {len(paragraphs)}")
print(f"Found {len(headings)} potential chapter headings.")
print("--- Sample Headings ---")
for h in headings[:30]:
    print(f"P#{h[0]}: {h[1]}")
