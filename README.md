<div align="center">

```
███╗   ██╗███████╗██╗   ██╗██████╗  ██████╗ ███╗   ██╗██╗██╗  ██╗
████╗  ██║██╔════╝██║   ██║██╔══██╗██╔═══██╗████╗  ██║██║╚██╗██╔╝
██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║   ██║██╔██╗ ██║██║ ╚███╔╝ 
██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║   ██║██║╚██╗██║██║ ██╔██╗ 
██║ ╚████║███████╗╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝
```

### ⚡ A blazing-fast, modular **Retrieval-Augmented Generation** framework

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Groq](https://img.shields.io/badge/LLM-Groq-F55036?style=for-the-badge&logo=groq&logoColor=white)](https://groq.com)
[![FAISS](https://img.shields.io/badge/VectorDB-FAISS-00B4D8?style=for-the-badge&logo=meta&logoColor=white)](https://github.com/facebookresearch/faiss)
[![FastAPI](https://img.shields.io/badge/API-FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

</div>

---

## 🧠 What is Neuronix?

> **Neuronix** is not just another RAG wrapper — it's a **production-ready framework** engineered from the ground up to give you full control over your retrieval pipeline.

Built with a **clean, modular architecture**, Neuronix lets you plug in any embedding model, vector store, or LLM — without rewriting a single line of your pipeline code. Fast. Flexible. Powerful.

---

## ✨ Features at a Glance

| | Feature | Description |
|---|---|---|
| 📄 | **Document Ingestion** | Load & chunk raw text files with intelligent overlap |
| 🔍 | **BGE Embeddings** | State-of-the-art `BAAI/bge-small-en-v1.5` dense vectors |
| ⚡ | **Multi-LLM Support** | Native integration with **Groq, OpenAI, and Gemini** |
| 🗂️ | **FAISS Vector Store** | Lightning-fast local similarity search with save/load |
| 🔌 | **Modular Design** | Swap any component via clean abstract base classes |
| 🌐 | **FastAPI REST API** | Production-ready `/ask` endpoint, plug & play |
| 🖥️ | **CLI Support** | Query your knowledge base directly from the terminal |

---

## 🏗️ Architecture

```
                         ┌─────────────────────────────────────┐
                         │           Neuronix Framework         │
                         └─────────────────────────────────────┘
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            │                             │                             │
     ┌──────▼──────┐             ┌────────▼────────┐           ┌───────▼──────┐
     │  INGESTION  │             │   VECTOR STORE  │           │     LLM      │
     │─────────────│             │─────────────────│           │──────────────│
     │ TextLoader  │──embed──►   │  FAISS Store    │ retrieve  │  GroqLLM     │
     │ DocSplitter │             │  (BGE Vectors)  │──────────►│  (llama-3.1) │
     └─────────────┘             └─────────────────┘           └──────┬───────┘
                                                                       │ generate
                                                                       ▼
                                                              ┌────────────────┐
                                                              │  RAG Pipeline  │
                                                              │   (Answer)     │
                                                              └────────────────┘
```

---

## 📁 Project Structure

```
Neuronix-framework-v1.0/
│
├── 📄 .env.example              ← Copy this to .env and add your API key
├── 📄 .gitignore
├── 📄 README.md
├── 🧪 test_run.py               ← Run this to test the full pipeline
│
└── 📦 neuronix/
    ├── 🔧 config/
    │   └── settings.py          ← All configuration via environment variables
    │
    ├── 🏛️ core/
    │   ├── types.py             ← Document, QueryResult data models
    │   ├── exceptions.py        ← LLMError, VectorStoreError, etc.
    │   └── logger.py            ← Framework-wide logging
    │
    ├── 📥 ingestion/
    │   ├── loader.py            ← TextLoader
    │   └── splitter.py          ← RecursiveCharacterTextSplitter
    │
    ├── 🧠 embeddings/
    │   ├── base.py              ← Abstract BaseEmbeddings
    │   └── bge.py               ← HuggingFace BGE implementation
    │
    ├── 🗄️ vectorstore/
    │   ├── base.py              ← Abstract BaseVectorStore
    │   └── faiss_store.py       ← FAISS implementation
    │
    ├── 🔎 retriever/
    │   ├── base.py              ← Abstract BaseRetriever
    │   └── dense_retriever.py   ← Dense vector retriever
    │
    ├── 🤖 llm/
    │   ├── __init__.py          ← Package exports & factory get_llm()
    │   ├── base.py              ← Abstract BaseLLM
    │   ├── groq_llm.py          ← Groq API client
    │   ├── openai_llm.py        ← OpenAI API client
    │   └── gemini_llm.py        ← Gemini API client
    │
    ├── 🔗 rag/
    │   └── pipeline.py          ← RAGPipeline orchestrator
    │
    └── 🌐 api/
        └── app.py               ← FastAPI REST application
```

---

## 🚀 Quick Start

### 1️⃣ Install Dependencies

```bash
pip install langchain langchain-community langchain-text-splitters \
            pydantic pydantic-settings sentence-transformers \
            faiss-cpu fastapi uvicorn groq
```

### 2️⃣ Configure Your API Key

```bash
# Copy the example file
cp .env.example .env
```

Then open `.env` and replace the placeholder:
```env
GROQ_API_KEY=your_groq_api_key_here
```

> 💡 Get your free Groq API key at [console.groq.com](https://console.groq.com)

### 3️⃣ Run the Test Pipeline

```bash
python test_run.py
```

Expected output:
```
INFO - Created sample knowledge file.
INFO - Loaded document from sample_knowledge.txt
INFO - Split 1 documents into 5 chunks
INFO - Initializing BGE embeddings with model BAAI/bge-small-en-v1.5
INFO - Added 5 documents to FAISS store
INFO - Saved FAISS index to faiss_index
INFO - Initialized Groq LLM with model llama-3.1-8b-instant
INFO - Query: What is Neuronix?
INFO - Answer: Neuronix is a new generation RAG framework...
INFO - Sources used: 2
```

### 4️⃣ Launch the REST API

```bash
uvicorn neuronix.api.app:app --reload
```

Query it with a POST request:
```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"query": "What is Neuronix?"}'
```

Response:
```json
{
  "answer": "Neuronix is a RAG framework designed for simplicity and power...",
  "sources": [...]
}
```

---

## ⚙️ Configuration Reference

All settings are controlled via environment variables (`.env` file):

| Variable | Default | Description |
|---|---|---|
| `DEFAULT_LLM_PROVIDER` | `groq` | Default LLM provider (`groq`, `openai`, `gemini`) |
| `GROQ_API_KEY` | `""` | Your Groq API key |
| `GROQ_MODEL_NAME` | `llama-3.1-8b-instant` | Groq model identifier |
| `OPENAI_API_KEY` | `""` | Your OpenAI API key |
| `OPENAI_MODEL_NAME` | `gpt-4o-mini` | OpenAI model identifier |
| `GEMINI_API_KEY` | `""` | Your Gemini API key |
| `GEMINI_MODEL_NAME` | `gemini-1.5-flash` | Google Gemini model identifier |
| `EMBEDDING_MODEL` | `BAAI/bge-small-en-v1.5` | HuggingFace embedding model |
| `CHUNK_SIZE` | `1000` | Characters per text chunk |
| `CHUNK_OVERLAP` | `200` | Overlap between chunks |
| `VECTOR_DB_PATH` | `faiss_index` | Local path for FAISS index |

---

## 🔌 Extending Neuronix

Neuronix is built around **abstract base classes**, making it trivially easy to swap components.

**Custom LLM?**
```python
from neuronix.llm.base import BaseLLM

class MyCustomLLM(BaseLLM):
    def generate(self, prompt: str) -> str:
        # your implementation here
        return my_model.predict(prompt)
```

**Custom Vector Store?**
```python
from neuronix.vectorstore.base import BaseVectorStore

class PineconeStore(BaseVectorStore):
    def add_documents(self, documents): ...
    def similarity_search(self, query, k=4): ...
    def save(self, path): ...
    def load(self, path): ...
```

Drop your class into the pipeline — no other changes needed. ✅

---

## 🗺️ Roadmap

- [x] Text file ingestion & chunking
- [x] BGE dense embeddings
- [x] FAISS vector store with persistence
- [x] Groq LLM integration
- [x] RAG pipeline orchestrator
- [x] FastAPI REST endpoint
- [ ] PDF & web URL loaders
- [ ] Hybrid search (dense + BM25)
- [ ] Re-ranking with cross-encoders
- [ ] Multi-turn conversation memory
- [ ] Streaming responses
- [ ] Docker support

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/your-feature`)
3. Commit your changes (`git commit -m "feat: add your feature"`)
4. Push and open a Pull Request

---

<div align="center">

**Built with ❤️ by [samay722](https://github.com/samay722)**

⭐ If you found this useful, please star the repo!

</div>