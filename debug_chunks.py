from ingest import read_pdf, chunk_text
from pathlib import Path

for page_number, text in read_pdf(Path("docs/ux_usability_heuristics.pdf")):
    for i, chunk in enumerate(chunk_text(text)):
        if "Visibility" in chunk:
            print(f"--- chunk {i} ---")
            print(chunk)