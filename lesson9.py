import math
import ollama

chunks = [
    "Xi lives in Malmö and has a dog.",
    "Python is a programming language used for AI.",
    "Karachi is a large city in Pakistan.",
    "SQLite is a small database stored in one file.",
]

def embed(texts):
    response = ollama.embed(model="nomic-embed-text", input=texts)
    return response["embeddings"]

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    return dot / (norm_a * norm_b)

chunk_vectors = embed(chunks)

question = "What is the capital of France?"
question_vector = embed([question])[0]

scores = [cosine(question_vector, v) for v in chunk_vectors]

for chunk, score in zip(chunks, scores):
    print(f"{score:.3f}  {chunk}")

best = chunks[scores.index(max(scores))]
print("Best chunk:", best)

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Answer using only the context provided. If the answer is not in the context, say you don't know."},
        {"role": "user", "content": f"Context: {best}\n\nQuestion: {question}"},
    ],
)
print("Answer:", response["message"]["content"])