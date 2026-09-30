import math
from pathlib import Path

import ollama

from ingest import read_pdf, chunk_text


def embed(texts):
    return ollama.embed(model="nomic-embed-text", input=texts)["embeddings"]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


def load_chunks():
    items = []
    for pdf_path in Path("docs").glob("*.pdf"):
        for page_number, text in read_pdf(pdf_path):
            for chunk in chunk_text(text):
                items.append({"text": chunk, "source": pdf_path.name, "page": page_number})
    return items


def retrieve(question, items, vectors, k=3):
    q_vec = embed(["search_query: " + question])[0]
    scored = [(cosine(q_vec, v), item) for v, item in zip(vectors, items)]
    scored.sort(key=lambda pair: pair[0], reverse=True)
    return scored[:k]


def answer(question, hits):
    context = "\n\n".join(
        f"[{item['source']}, page {item['page']}]\n{item['text']}" for _, item in hits
    )
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "system", "content": "Answer using only the context provided. If the answer is not in the context, say you don't know. Mention the source file names you used."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
    )
    return response["message"]["content"]

def main():
    items = load_chunks()
    print(f"Embedding {len(items)} chunks...")
    vectors = embed(["search_document: " + item["text"] for item in items])
    MIN_SCORE = 0.55

    while True:
        question = input("\nAsk a question (or type quit): ")
        if question.strip().lower() == "quit":
            break
        hits = retrieve(question, items, vectors)
        if hits[0][0] < MIN_SCORE:
            print("I couldn't find anything relevant in the documents.")
            continue
        print(answer(question, hits))
        print("\nSources:")
        for score, item in hits:
            print(f"  {score:.2f}  {item['source']} (page {item['page']})")

if __name__ == "__main__":
    main()
