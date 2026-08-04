import zipfile
import sys

docx_path = sys.argv[1] if len(sys.argv) > 1 else "Materialist Christianity EBook.docx"
with zipfile.ZipFile(docx_path) as z:
    print("Files in ZIP archive:")
    for name in z.namelist():
        print(name)
