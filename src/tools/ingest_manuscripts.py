import sys
import os
import re
import yaml
from datetime import datetime

sys.path.insert(0, os.path.abspath("."))
from src.tools.docx_reader import extract_text_from_docx

def clean_xml_tags(text: str) -> str:
    """Removes remaining embedded Word XML tags from extracted text strings."""
    cleaned = re.sub(r'<[^>]+>', '', text)
    return cleaned.strip()

def ingest_volume_ii(docx_path: str = "Materialist_Christianity_Volume_II_EBook_9798999800640.docx"):
    output_dir = os.path.join("okf", "graph", "manuscripts")
    os.makedirs(output_dir, exist_ok=True)

    text = extract_text_from_docx(docx_path)
    paragraphs = text.split("\n\n")

    parts = [
        {"id": "vol2_part1", "title": "Part 1: Reconstructing the Lens", "start": 183, "end": 492},
        {"id": "vol2_part2", "title": "Part 2: The Foundations of Operation", "start": 493, "end": 749},
        {"id": "vol2_part3", "title": "Part 3: The Fractured Self", "start": 750, "end": 1149},
        {"id": "vol2_part4", "title": "Part 4: The Covenant Substrate", "start": 1150, "end": 1433},
        {"id": "vol2_part5", "title": "Part 5: The Realized Code", "start": 1434, "end": len(paragraphs)},
    ]

    now = datetime.now().isoformat()

    for p_info in parts:
        section_paras = paragraphs[p_info["start"]:p_info["end"]]
        cleaned_paras = [clean_xml_tags(p) for p in section_paras if clean_xml_tags(p)]
        section_text = "\n\n".join(cleaned_paras)

        frontmatter = {
            "id": f"okf:manuscript:{p_info['id']}",
            "type": "ManuscriptSection",
            "title": f"Materialist Christianity Vol II - {p_info['title']}",
            "author": "Ezra Byrd",
            "copyright": "2026 Ezra Byrd",
            "isbn_paperback": "979-8-9998006-6-4",
            "isbn_ebook": "979-8-9998006-4-0",
            "word_count": len(section_text.split()),
            "created_at": now,
            "relations": [
                {
                    "target_id": "okf:experiment:EXP-001",
                    "relationship_type": "DERIVED_FROM"
                }
            ]
        }

        content = f"""---
{yaml.dump(frontmatter, sort_keys=False)}---

# {p_info['title']}

{section_text[:1500]} ... [Section Continues]
"""
        file_path = os.path.join(output_dir, f"{p_info['id']}.md")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Ingested {p_info['id']}: {p_info['title']} ({len(section_text.split())} words)")

if __name__ == "__main__":
    ingest_volume_ii()
