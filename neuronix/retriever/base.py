from abc import ABC, abstractmethod
from typing import List
from neuronix.core.types import Document

class BaseRetriever(ABC):
    @abstractmethod
    def retrieve(self, query: str) -> List[Document]:
        pass
