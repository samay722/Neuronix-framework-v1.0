import os
from neuronix.config.settings import settings
from neuronix.embeddings.bge import BGEEmbeddings
from neuronix.vectorstore.faiss_store import FAISSVectorStore
from neuronix.retriever.dense_retriever import DenseRetriever
from neuronix.retriever.bm25_retriever import BM25Retriever
from neuronix.retriever.hybrid_retriever import HybridRetriever
from neuronix.reranker.bge_reranker import BGEReranker
from neuronix.query.rewriter import QueryRewriter
from neuronix.llm.groq_llm import GroqLLM
from neuronix.rag.pipeline import RAGPipeline
from neuronix.core.types import Document

# Sample knowledge base documents
documents_text = [
    "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.",
    "Neuronix is a next-generation RAG framework designed for simplicity, modularity, and power. It integrates FAISS and Groq.",
    "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability.",
    "FAISS is a library for efficient similarity search and clustering of dense vectors."
]

def main():
    print("=== Initializing components for RAG Pipeline test ===")
    
    # 1. Embeddings & Vector Store
    embeddings = BGEEmbeddings(model_name=settings.EMBEDDING_MODEL)
    vectorstore = FAISSVectorStore(embeddings=embeddings)
    
    docs = [Document(page_content=text, metadata={"source": "test_data"}) for text in documents_text]
    vectorstore.add_documents(docs)
    vectorstore.save(settings.VECTOR_DB_PATH)
    
    # 2. Retrievers
    dense_retriever = DenseRetriever(vectorstore=vectorstore, k=4)
    bm25_retriever = BM25Retriever(documents_text)
    hybrid_retriever = HybridRetriever(
        dense_retriever=dense_retriever,
        bm25_retriever=bm25_retriever
    )
    
    # 3. Reranker & Rewriter & LLM
    reranker = BGEReranker()
    llm = GroqLLM()  # Defaults to settings/env
    rewriter = QueryRewriter(llm)
    
    # 4. RAG Pipeline
    rag = RAGPipeline(
        retriever=hybrid_retriever,
        reranker=reranker,
        rewriter=rewriter,
        llm=llm
    )
    
    # 5. Query
    query = "What is FastAPI?"
    print(f"\nUser Query: {query}")
    print("Running pipeline...")
    
    answer = rag.run(query)
    print("\n--- Pipeline Answer ---")
    print(answer)
    print("------------------------")

if __name__ == "__main__":
    main()
