from typing import List
from neuronix.retriever.base import BaseRetriever
from neuronix.vectorstore.base import BaseVectorStore
from neuronix.core.types import Document
from neuronix.core.logger import logger

class DenseRetriever(BaseRetriever):
    def __init__(self, vectorstore: BaseVectorStore, k: int = 4):
        self.vectorstore = vectorstore
        self.k = k
        
    def retrieve(self, query: str) -> List[Document]:
        logger.info(f"Retrieving top {self.k} documents for query: '{query}'")
        return self.vectorstore.similarity_search(query, k=self.k)
