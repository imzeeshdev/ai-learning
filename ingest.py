from pathlib import Path
from pypdf import PdfReader

def read_pdf(path):
    reader = PdfReader(path)
    pages = []
    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        pages.append((page_number, text))
    return pages

def chunk_text(text, size=800, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks

if __name__ == "__main__":
    for pdf_path in Path("docs").glob("*.pdf"):
        pages = read_pdf(pdf_path)
        total = 0
        for page_number, text in pages:
            total += len(chunk_text(text))
        print(f"{pdf_path.name}: {len(pages)} pages, {total} chunks")