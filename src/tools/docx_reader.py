import zipfile
import re
import os

def extract_text_from_docx(docx_path: str) -> str:
    """Extracts text from docx xml tags using regex pattern matching."""
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"File not found: {docx_path}")

    with zipfile.ZipFile(docx_path) as z:
        xml_content = z.read("word/document.xml").decode("utf-8", errors="ignore")

    # Match text inside <w:t ...>text</w:t> or <w:t>text</w:t>
    text_matches = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml_content)
    
    # Reconstruct text with paragraph breaks
    paragraphs = []
    current_para = []
    
    # Split XML by paragraph tags <w:p> or </w:p>
    p_blocks = re.split(r'</?w:p[^>]*>', xml_content)
    for p in p_blocks:
        t_in_p = re.findall(r'<w:t[^>]*>(.*?)</w:t>', p)
        if t_in_p:
            paragraphs.append(''.join(t_in_p))

    return '\n\n'.join(paragraphs)

if __name__ == "__main__":
    import sys
    file_path = sys.argv[1] if len(sys.argv) > 1 else "Materialist Christianity EBook.docx"
    text = extract_text_from_docx(file_path)
    print(f"Extracted {len(text)} characters from {file_path}")
    print("--- First 600 characters ---")
    print(text[:600])
