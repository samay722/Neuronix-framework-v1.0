import sys
import argparse
from neuronix.config.settings import settings
from neuronix.core.logger import logger
from neuronix.embeddings.bge import BGEEmbeddings
from neuronix.vectorstore.faiss_store import FAISSVectorStore
from neuronix.retriever.dense_retriever import DenseRetriever
from neuronix.llm import get_llm
from neuronix.rag.pipeline import RAGPipeline

def init_pipeline(llm_provider: str = None):
    logger.info("Initializing dependencies for pipeline...")
    embeddings = BGEEmbeddings(model_name=settings.EMBEDDING_MODEL)
    vectorstore = FAISSVectorStore(embeddings=embeddings)
    
    # Try to load existing index if present
    vectorstore.load(settings.VECTOR_DB_PATH)
    
    retriever = DenseRetriever(vectorstore=vectorstore)
    
    provider = llm_provider or settings.DEFAULT_LLM_PROVIDER
    llm = get_llm(provider)
    
    pipeline = RAGPipeline(retriever=retriever, llm=llm)
    return pipeline

def main():
    parser = argparse.ArgumentParser(description="Neuronix CLI")
    parser.add_argument("--query", type=str, help="Question to ask the RAG system")
    parser.add_argument("--llm", type=str, default=None, help="LLM provider to use (groq, openai, gemini)")
    args = parser.parse_args()
    
    if not args.query:
        print("Please provide a query using --query \"your question\"")
        sys.exit(1)
        
    pipeline = init_pipeline(llm_provider=args.llm)
    result = pipeline.query(args.query)
    
    print("\n--- Answer ---")
    print(result.answer)
    print("\n--- Sources ---")
    for doc in result.source_documents:
        print(f"[{doc.metadata.get('source', 'unknown')}]: {doc.page_content[:100]}...")

if __name__ == "__main__":
    main()
