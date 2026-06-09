import os
from neuronix.config.settings import settings
from neuronix.core.logger import logger
from neuronix.ingestion.loader import TextLoader
from neuronix.ingestion.splitter import DocumentSplitter
from neuronix.embeddings.bge import BGEEmbeddings
from neuronix.vectorstore.faiss_store import FAISSVectorStore
from neuronix.retriever.dense_retriever import DenseRetriever
from neuronix.llm.groq_llm import GroqLLM
from neuronix.rag.pipeline import RAGPipeline

def test_workflow():
    # 1. Create a dummy file for testing
    test_file_path = "sample_knowledge.txt"
    with open(test_file_path, "w", encoding="utf-8") as f:
        f.write("Neuronix is a new generation RAG framework designed for simplicity and power. It integrates with Groq for fast LLM inference and uses FAISS for vector storage.")
        
    logger.info("Created sample knowledge file.")

    try:
        # 2. Ingest
        loader = TextLoader(test_file_path)
        docs = loader.load()
        
        splitter = DocumentSplitter(chunk_size=50, chunk_overlap=10)
        chunks = splitter.split_documents(docs)
        
        # 3. Embed & Store
        embeddings = BGEEmbeddings(model_name=settings.EMBEDDING_MODEL)
        vectorstore = FAISSVectorStore(embeddings=embeddings)
        vectorstore.add_documents(chunks)
        vectorstore.save(settings.VECTOR_DB_PATH)
        
        # 4. Retrieve & Generate
        retriever = DenseRetriever(vectorstore=vectorstore, k=2)
        llm = GroqLLM() # Ensure GROQ_API_KEY is set in environment!
        
        pipeline = RAGPipeline(retriever=retriever, llm=llm)
        
        # 5. Query
        query = "What is Neuronix?"
        result = pipeline.query(query)
        
        logger.info(f"Query: {query}")
        logger.info(f"Answer: {result.answer}")
        logger.info(f"Sources used: {len(result.source_documents)}")
        
    except Exception as e:
        logger.error(f"Test run failed: {str(e)}")
    finally:
        # Clean up
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

if __name__ == "__main__":
    test_workflow()
