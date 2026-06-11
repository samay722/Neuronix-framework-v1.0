from typing import List
from neuronix.core.types import QueryResult, Document
from neuronix.retriever.base import BaseRetriever
from neuronix.llm.base import BaseLLM
from neuronix.core.logger import logger

class RAGPipeline:
    def __init__(
        self, 
        retriever: BaseRetriever, 
        llm: BaseLLM,
        reranker = None,
        rewriter = None
    ):
        self.retriever = retriever
        self.llm = llm
        self.reranker = reranker
        self.rewriter = rewriter
        
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

    def run(self, query: str, top_k: int = 5) -> str:
        logger.info(f"Running full RAG pipeline for query: {query}")
        
        # 1. Rewrite query if rewriter is present
        if self.rewriter:
            rewritten_query = self.rewriter.rewrite(query)
            logger.info(f"Rewritten query: {rewritten_query}")
        else:
            rewritten_query = query

        # 2. Retrieve documents
        try:
            retrieved_docs = self.retriever.retrieve(rewritten_query, top_k=20)
        except TypeError:
            retrieved_docs = self.retriever.retrieve(rewritten_query)

        documents = [doc.page_content for doc in retrieved_docs]

        # 3. Rerank if reranker is present
        if self.reranker and documents:
            reranked = self.reranker.rerank(
                query=rewritten_query,
                documents=documents,
                top_k=top_k
            )
            context = "\n\n".join([doc for doc, _ in reranked])
        else:
            context = "\n\n".join(documents[:top_k])

        # 4. Final prompt
        prompt = f"""
You are a helpful assistant.

Use ONLY the context below to answer.

Context:
{context}

Question:
{query}

Answer:
"""

        # 5. LLM call
        return self.llm.generate(prompt)
