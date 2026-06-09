from abc import ABC, abstractmethod
from typing import List, Tuple, Optional
from neuronix.core.types import Document

class BaseVectorStore(ABC):
    @abstractmethod
    def add_documents(self, documents: List[Document]) -> None:
        pass
        
    @abstractmethod
    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        pass
        
    @abstractmethod
    def save(self, path: str) -> None:
        pass
        
    @abstractmethod
    def load(self, path: str) -> None:
        pass
