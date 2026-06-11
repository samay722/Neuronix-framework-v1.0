from typing import List
from rank_bm25 import BM25Okapi
from neuronix.retriever.base import BaseRetriever
from neuronix.core.types import Document


class BM25Retriever(BaseRetriever):

    def __init__(self, documents):

        self.documents = documents

        tokenized_docs = [
            doc.lower().split()
            for doc in documents
        ]

        self.bm25 = BM25Okapi(tokenized_docs)

    def retrieve(self, query: str, top_k: int = 5) -> List[Document]:

        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked_docs = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        results = []

        for doc_text, score in ranked_docs[:top_k]:
            results.append(
                Document(
                    page_content=doc_text,
                    metadata={"score": float(score), "source": "bm25"}
                )
            )

        return results