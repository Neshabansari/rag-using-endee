import subprocess

def generate_answer(question, context):
    prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        text=True,
        encoding="utf-8",     
        errors="ignore",       
        capture_output=True
    )

    return result.stdout.strip()
