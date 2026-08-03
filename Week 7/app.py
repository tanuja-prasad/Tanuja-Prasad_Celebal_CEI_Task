import os
import streamlit as st
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer
from transformers import pipeline


# Page Configuration

st.set_page_config(
    page_title="RAG Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Document Question Answering System (RAG)")
st.write("Ask questions about your AI documents.")


# Load Documents

documents = ""
folder = "data"

for file in os.listdir(folder):
    if file.endswith(".txt"):
        with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
            documents += f.read() + "\n"

# Create Chunks

chunk_size = 300
chunks = []

for i in range(0, len(documents), chunk_size):
    chunks.append(documents[i:i + chunk_size])


# Embedding Model

@st.cache_resource
def load_embedding_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

embedding_model = load_embedding_model()

embeddings = embedding_model.encode(chunks)


# FAISS

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))


# Load LLM

@st.cache_resource
def load_generator():
    return pipeline(
        "text2text-generation",
        model="google/flan-t5-base"
    )

generator = load_generator()

# Ask Function

def ask_question(question):

    question_embedding = embedding_model.encode([question])

    distances, indices = index.search(
        np.array(question_embedding).astype("float32"),
        k=3
    )

    context = ""

    for idx in indices[0]:
        context += chunks[idx] + "\n"

    prompt = f"""
Answer ONLY using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = generator(
        prompt,
        max_new_tokens=100,
        do_sample=False
    )

    return response[0]["generated_text"]


# Chat History

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
question = st.chat_input("Ask a question...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    answer = ask_question(question)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)