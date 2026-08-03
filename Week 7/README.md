# 📚 Document Question Answering System using RAG

## 📖 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that answers user questions based on custom documents.

Unlike traditional language models that rely only on pre-trained knowledge, this system retrieves the most relevant information from user-provided documents before generating an answer. This makes the responses more accurate, context-aware, and useful for private or domain-specific data.

---

## 🎯 Objectives

- Understand the concept of Retrieval-Augmented Generation (RAG)
- Build a complete document question answering pipeline
- Retrieve relevant information from custom documents
- Generate context-aware answers using retrieved information
- Learn how embeddings and vector databases work together

---

## 🚀 Features

- Load multiple text documents
- Split documents into smaller chunks
- Generate semantic embeddings
- Store embeddings in a FAISS vector database
- Retrieve the most relevant document chunks
- Generate answers based on retrieved context
- Simple ChatGPT-like interface using Streamlit

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Hugging Face Transformers
- NumPy

---

## 📂 Project Structure

```text
Document-QA-RAG/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── ai.txt
│   ├── machine_learning.txt
│   └── deep_learning.txt
│
└── screenshots/
```

---

## 📊 Workflow

```
Documents (TXT/PDF)
        │
        ▼
Document Loading
        │
        ▼
Text Chunking
        │
        ▼
Embedding Generation
(Sentence Transformers)
        │
        ▼
FAISS Vector Database
        │
───────────────
User Question
        │
        ▼
Question Embedding
        │
        ▼
Similarity Search
        │
        ▼
Top Relevant Chunks
        │
        ▼
Language Model
        │
        ▼
Generated Answer
```

---

## ⚙️ How It Works

### 1. Document Ingestion

The system loads one or more text documents containing information.

### 2. Text Chunking

Large documents are divided into smaller chunks for better retrieval accuracy.

### 3. Embedding Creation

Each text chunk is converted into a numerical vector using the **Sentence Transformer** embedding model.

### 4. Vector Database

The embeddings are stored inside a **FAISS** vector database.

### 5. User Query

The user enters a question through the Streamlit interface.

### 6. Retrieval

The query is converted into an embedding and compared with stored vectors.

The top-k most relevant chunks are retrieved.

### 7. Answer Generation

The retrieved chunks are provided as context to the language model, which generates the final answer.

---

## 📁 Dataset

The project uses custom text documents.

Example files:

- ai.txt
- machine_learning.txt
- deep_learning.txt

The same pipeline can also work with:

- PDF Notes
- Research Papers
- Books
- Resume
- Company Documents

---

## 💬 Sample Questions

- What is Artificial Intelligence?
- What are the applications of AI?
- Explain Machine Learning.
- What is Deep Learning?
- What is CNN?
- What are Transformers?
- Difference between AI and Machine Learning?
- Explain supervised learning.

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/document-qa-rag.git
```

Move into the project directory

```bash
cd document-qa-rag
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Output

The application provides a ChatGPT-style interface where users can ask questions related to uploaded documents.

Example:

**User**

```
What is Machine Learning?
```

**Assistant**

```
Machine Learning is a subset of Artificial Intelligence
that enables computers to learn patterns from data
without being explicitly programmed.
```

---

## 🔮 Future Improvements

- Support PDF documents
- Upload documents from the UI
- Better chunking strategies
- Hybrid search (Keyword + Vector Search)
- Conversation memory
- Multiple embedding models
- Re-ranking retrieved results
- Deploy on Streamlit Cloud

---

## 📚 Key Learnings

- Retrieval-Augmented Generation (RAG)
- Text preprocessing
- Semantic embeddings
- Vector databases
- Similarity search
- Context-aware question answering
- Streamlit application development

---

## 👨‍💻 Author

**Tanuja Prasad**

MCA Student | Data Science Enthusiast
