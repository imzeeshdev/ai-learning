import ollama

context = "Xi lives in Malmö and has a dog."

question = "What is Xi's favorite color?"

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "system", "content": "Answer using only the context provided."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {question}"},
    ],
)
print(response["message"]["content"])
