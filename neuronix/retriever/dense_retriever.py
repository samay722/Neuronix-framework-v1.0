from typing import List
from neuronix.retriever.base import BaseRetriever
from neuronix.vectorstore.base import BaseVectorStore
from neuronix.core.types import Document
from neuronix.core.logger import logger

class DenseRetriever(BaseRetriever):
    def __init__(self, vectorstore: BaseVectorStore, k: int = 4):
        self.vectorstore = vectorstore
        self.k = k
        
    def retrieve(self, query: str, top_k: int = None) -> List[Document]:
        k = top_k or self.k
        logger.info(f"Retrieving top {k} documents for query: '{query}'")
        return self.vectorstore.similarity_search(query, k=k)
