from embedding import generate_embeddings
from endee_store import EndeeVectorStore
from llm import generate_answer   

def load_documents(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f.readlines() if line.strip()]

def main():
    print("Indexing documents...")

    documents = load_documents("data/documents.txt")

    doc_embeddings = generate_embeddings(documents)

    vector_store = EndeeVectorStore()
    vector_store.add_documents(documents, doc_embeddings)

    print("Indexing completed successfully!\n")

    while True:
        question = input("Ask a question (or type 'exit'): ")
        if question.lower() == "exit":
            break

        query_embedding = generate_embeddings([question])[0]

        retrieved_docs = vector_store.search(query_embedding)

        context = "\n".join(retrieved_docs)

        answer = generate_answer(question, context)

        print("\nAnswer:")
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    main()
