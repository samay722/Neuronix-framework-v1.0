from typing import List
from neuronix.retriever.base import BaseRetriever
from neuronix.core.types import Document


class HybridRetriever(BaseRetriever):

    def __init__(
        self,
        dense_retriever,
        bm25_retriever
    ):
        self.dense = dense_retriever
        self.bm25 = bm25_retriever

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ) -> List[Document]:

        dense_results = self.dense.retrieve(
            query,
            top_k=top_k
        )

        bm25_results = self.bm25.retrieve(
            query,
            top_k=top_k
        )

        combined = {}

        for doc in dense_results:
            combined[doc.page_content] = {
                "document": doc,
                "score": 1.0  # Default score for dense match
            }

        for doc in bm25_results:
            bm25_score = doc.metadata.get("score", 0.0)
            if doc.page_content in combined:
                combined[doc.page_content]["score"] += bm25_score
            else:
                combined[doc.page_content] = {
                    "document": doc,
                    "score": bm25_score
                }

        ranked = sorted(
            combined.values(),
            key=lambda x: x["score"],
            reverse=True
        )

        return [item["document"] for item in ranked[:top_k]]