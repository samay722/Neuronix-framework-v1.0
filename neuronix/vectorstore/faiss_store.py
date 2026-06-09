import os
from typing import List, Tuple, Optional
from langchain_community.vectorstores import FAISS
from neuronix.vectorstore.base import BaseVectorStore
from neuronix.core.types import Document
from neuronix.embeddings.base import BaseEmbeddings
from neuronix.core.logger import logger
from langchain_core.documents import Document as LCDocument

class FAISSVectorStore(BaseVectorStore):
    def __init__(self, embeddings: BaseEmbeddings):
        self.embeddings = embeddings
        self.store = None
        self.lc_embeddings = getattr(embeddings, "embeddings", None)
        if not self.lc_embeddings:
            logger.warning("FAISSStore expects an embedding wrapper that has a .embeddings property of langchain type.")
            
    def _to_lc_documents(self, documents: List[Document]) -> List[LCDocument]:
        return [LCDocument(page_content=doc.page_content, metadata=doc.metadata) for doc in documents]
        
    def _from_lc_documents(self, lc_docs: List[LCDocument]) -> List[Document]:
        return [Document(page_content=doc.page_content, metadata=doc.metadata) for doc in lc_docs]

    def add_documents(self, documents: List[Document]) -> None:
        lc_docs = self._to_lc_documents(documents)
        if self.store is None:
            self.store = FAISS.from_documents(lc_docs, self.lc_embeddings)
        else:
            self.store.add_documents(lc_docs)
        logger.info(f"Added {len(documents)} documents to FAISS store")

    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        if self.store is None:
            logger.error("Cannot search an empty vector store")
            return []
            
        lc_docs = self.store.similarity_search(query, k=k)
        return self._from_lc_documents(lc_docs)

    def save(self, path: str) -> None:
        if self.store is not None:
            self.store.save_local(path)
            logger.info(f"Saved FAISS index to {path}")
            
    def load(self, path: str) -> None:
        if os.path.exists(path):
            self.store = FAISS.load_local(path, self.lc_embeddings, allow_dangerous_deserialization=True)
            logger.info(f"Loaded FAISS index from {path}")
        else:
            logger.warning(f"FAISS index path {path} does not exist.")
