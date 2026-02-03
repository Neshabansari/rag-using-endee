# RAG Application using Endee Vector Database

**Author:** Neshab Alam Ansari  
**Affiliation:** SRM University, AP  
**Email:** [neshabalam_ansari@srmap.edu.in]  

---

##  Project Overview

This project implements a **Retrieval Augmented Generation (RAG)** system that allows users to ask questions and receive answers grounded strictly in a given set of documents.

The core idea is to combine:
- **Semantic search** using vector embeddings
- **Endee** as the vector database
- **A local Large Language Model (LLM)** for answer generation

By retrieving only the most relevant documents and using them as context, the system avoids hallucinations and provides accurate, context-aware responses.

---

##  Problem Statement

Traditional language models generate answers based on general knowledge and may produce incorrect or hallucinated responses.

This project addresses that problem by:
- Retrieving relevant information from a **custom document set**
- Restricting the LLM to answer **only using retrieved context**
- Ensuring responses are explainable, accurate, and grounded

---

##  Use Case Demonstrated

- **Retrieval Augmented Generation (RAG)**  
- **Semantic Search using vector similarity**

Vector search is the core of this application, making it suitable for:
- Knowledge base Q&A
- Internal document search
- Educational or enterprise AI assistants

---

##  System Design / Technical Approach

### High-Level Architecture

```
User Question
↓
Text Embedding (Sentence Transformers)
↓
Vector Search (Endee)
↓
Relevant Documents (Context)
↓
Local LLM (Ollama)
↓
Final Answer
```



---

### Step-by-Step Flow

1. **Document Ingestion**
   - Text documents are loaded from a file.
   - Each document is converted into a vector embedding.

2. **Vector Storage**
   - Embeddings are stored using **Endee**.
   - Endee enables efficient similarity search over vectors.

3. **Query Processing**
   - User query is converted into an embedding.
   - Endee performs vector similarity search to retrieve relevant documents.

4. **Answer Generation**
   - Retrieved documents are passed as context to a local LLM.
   - The model generates an answer strictly based on that context.

---

##  How Endee is Used

**Endee acts as the vector database in this project.**

Specifically:
- Stores document embeddings
- Performs semantic similarity search
- Returns the most relevant documents for a given query

Endee is used as the **core retrieval layer**, making it central to the RAG workflow.

This project uses Endee via its Python interface to:
- Add vectors to the store
- Search vectors during query time

Repository reference:  
👉 https://github.com/EndeeLabs/endee

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Vector Database:** Endee  
- **Embedding Model:** Sentence Transformers (`all-MiniLM-L6-v2`)  
- **LLM:** Local LLM via Ollama  
- **UI:** Streamlit  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-github-repo-link>
cd rag-using-endee

```

### 2️⃣ Create and Activate Virtual Environment
python -m venv venv

### Windows
venv\Scripts\activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt
 
### 4️⃣ Install Ollama (Local LLM)
Download and install Ollama from:
https://ollama.com/download

Pull the model:
ollama pull llama3

### 5️⃣ Run the Application (UI)
streamlit run app.py
The application will open automatically in the browser.

### ▶️ How to Use

1. Wait for the application to load.
2. Enter a question in the input box.
3. Click the Ask button.
4. The system retrieves relevant documents using Endee and generates an answer.

### ✅ Key Features
Uses Endee as the vector database

- Prevents hallucinations by enforcing context-based answers
- Fully local (no API keys required)
- Clean and interactive UI
- Optimized with embedding and vector-store caching

  
###  Project Structure

```
rag-using-endee/
├── app.py                # Streamlit UI
├── src/
│   ├── embedding.py      # Embedding generation
│   ├── endee_store.py    # Endee vector store logic
│   ├── llm.py            # Local LLM integration
│   └── main.py           # CLI-based RAG flow
├── data/
│   └── documents.txt     # Knowledge base
├── requirements.txt
└── README.md
```

### Conclusion

This project demonstrates a complete RAG pipeline where vector search is the core component, implemented using Endee.

It showcases:
- Practical AI/ML system design
- Clean separation of embedding, retrieval, and generation
- Real-world applicability for document-based AI systems



## License
MIT License
Copyright (c) 2025 Neshab Alam Ansari
