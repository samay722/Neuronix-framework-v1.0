from abc import ABC, abstractmethod


class BaseReranker(ABC):

    @abstractmethod
    def rerank(
        self,
        query,
        documents,
        top_k=5
    ):
        pass