

# 📚 LLM-Powered PDF Q\&A App

This project is an interactive Question Answering (QA) application built using **LangChain**, **Ollama (LLaMA 3.2 model)**, and **Streamlit**. It enables users to ask natural language questions about the content of a PDF document and get context-aware answers.

## 🚀 Features

* 🔍 Loads and processes PDF documents using `PyPDFLoader`
* 🧠 Uses Ollama's LLaMA 3.2 model for:

  * Embedding generation
  * Language understanding and response
* 🔗 Combines LangChain's prompt templates, retrievers, and output parsers
* 💬 Real-time Q\&A through a Streamlit web interface

## 🧰 Tech Stack

* **Python**
* **LangChain**
* **Ollama (LLaMA 3.2)**
* **Streamlit**

## 🛠️ How It Works

1. **Document Ingestion**: Loads a PDF (`attention.pdf`) and splits it into pages.
2. **Embeddings**: Generates vector embeddings using `OllamaEmbeddings`.
3. **Vector Store**: Stores embeddings in an in-memory vector database.
4. **Retrieval**: Retrieves the most relevant chunks of text based on the user’s question.
5. **Prompting**: Uses a customizable prompt template to guide the language model.
6. **Answer Generation**: Produces and displays a final answer using the LLaMA model.

## 📄 Usage

To run the app:

```bash
streamlit run stream.py
```

## 📁 File Structure

* `Project_01.py` – Core logic for PDF processing, embedding, retrieval, and QA chain.
* `stream.py` – Streamlit UI wrapper to run the app.
* `pyvenv.cfg` – (Optional) Virtual environment configuration.

## ✅ Requirements

* `langchain`
* `streamlit`
* `ollama`
* `PyPDFLoader`
* `docarray`

Make sure Ollama and the LLaMA 3.2 model are properly installed and running.

---
