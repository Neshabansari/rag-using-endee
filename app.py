import streamlit as st
from src.embedding import generate_embeddings
from src.endee_store import EndeeVectorStore
from src.llm import generate_answer

loading_placeholder = st.empty()
loading_placeholder.info("🔄 Loading application, please wait...")


@st.cache_resource(show_spinner=False)
def setup_vector_store():
    with open("data/documents.txt", "r", encoding="utf-8") as f:
        documents = [line.strip() for line in f.readlines() if line.strip()]

    embeddings = generate_embeddings(documents)

    store = EndeeVectorStore()
    store.add_documents(documents, embeddings)
    return store

st.set_page_config(page_title="RAG using Endee", layout="centered")

st.title("📄 RAG Application using Endee + Local LLM (Ollama)")
st.write("Ask questions based on the indexed documents.")

vector_store = setup_vector_store()

loading_placeholder.empty()

question = st.text_input("Ask a question:")

ask_clicked = st.button("Ask")

if ask_clicked and question:
    status_placeholder = st.empty()

    with status_placeholder:
        st.warning("⏳ Generating answer, please wait...")

    query_embedding = generate_embeddings([question])[0]
    docs = vector_store.search(query_embedding)
    context = "\n".join(docs)

    answer = generate_answer(question, context)

    status_placeholder.empty()

    st.subheader("Answer")
    st.write(answer)

