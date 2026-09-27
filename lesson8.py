import ollama

context = "RAG (Retrieval-Augmented Generation) is a technique where a program first retrieves relevant documents, then gives them to an LLM along with the question so the answer is based on those documents."

question = "In one sentence, what is RAG?"

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Answer using only the context provided."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"},
    ],
)
print(response["message"]["content"])
