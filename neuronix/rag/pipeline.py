from typing import List
from neuronix.core.types import QueryResult, Document
from neuronix.retriever.base import BaseRetriever
from neuronix.llm.base import BaseLLM
from neuronix.core.logger import logger

class RAGPipeline:
    def __init__(self, retriever: BaseRetriever, llm: BaseLLM):
        self.retriever = retriever
        self.llm = llm
        
    def _build_prompt(self, query: str, context: List[Document]) -> str:
        context_str = "\n\n".join([f"Source ({doc.metadata.get('source', 'unknown')}):\n{doc.page_content}" for doc in context])
        prompt = f"""You are a helpful AI assistant. Answer the user's question based ONLY on the following context.
If the answer cannot be found in the context, say "I cannot answer this based on the provided context."

Context:
{context_str}

Question:
{query}

Answer:"""
        return prompt

    def query(self, query_text: str) -> QueryResult:
        logger.info(f"Processing RAG query: {query_text}")
        
        # 1. Retrieve relevant documents
        docs = self.retriever.retrieve(query_text)
        
        # 2. Build prompt
        prompt = self._build_prompt(query_text, docs)
        
        # 3. Generate answer
        answer = self.llm.generate(prompt)
        
        return QueryResult(answer=answer, source_documents=docs)
