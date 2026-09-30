# RAG over PDFs

A small retrieval-augmented generation (RAG) app. It reads PDF documents, finds the most relevant passages for a question using embeddings, and asks a local LLM to answer using only those passages, with sources cited.

Built as a learning project while training to become an AI engineer.

## How it works

1. `ingest.py` reads PDFs from `docs/` and splits them into overlapping text chunks.
2. `rag.py` embeds each chunk with a local embedding model, embeds the question the same way, and finds the closest chunks by cosine similarity.
3. If the best match is too weak, the app says it doesn't know rather than guessing.
4. Otherwise, it sends the matched chunks to a local LLM and prints the answer with its sources.

## Setup

Requires [Ollama](https://ollama.com) running locally.

ollama pull llama3.2
ollama pull nomic-embed-text

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

## Run

python3 rag.py


Ask a question, or type `quit` to exit.

## Evaluate

`eval.py` checks retrieval against 10 test questions with known-correct source files.

python3 eval.py


### Results

Diagnosing and fixing retrieval quality was the main part of this project. Two changes were tested independently, each measured against the same 10-question set:

| Version | Top-1 correct | Top-3 contains it | Wrongly refused |
| --- | --- | --- | --- |
| Baseline (800-char chunks, no prefix) | 9/10 | 10/10 | 2/10 |
| + embedding prefixes (`search_query:` / `search_document:`) | 9/10 | 10/10 | 0/10 |
| + smaller chunks (350 chars) | 10/10 | 10/10 | 0/10 |

The one persistent failure (a question about a UX heuristic) turned out to be caused by chunks that mixed an introductory paragraph with several distinct topics, which diluted the embedding for any single topic. Reducing chunk size fixed it.

## Sample documents

`docs/` contains five short sample PDFs (PLM change management, UX heuristics, dog care, a Malmö newcomer guide, and a Swedish study guide) so the app runs out of the box.

