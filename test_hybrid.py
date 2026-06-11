from neuronix.retriever.bm25_retriever import BM25Retriever
from neuronix.retriever.hybrid_retriever import HybridRetriever


# Temporary Fake Dense Retriever
class FakeDenseRetriever:

    def retrieve(
        self,
        query,
        top_k=5
    ):

        return [
            {
                "document":
                "FastAPI is used to build APIs",
                "score": 0.7
            },
            {
                "document":
                "Python is a programming language",
                "score": 0.4
            }
        ]


docs = [
    "Artificial Intelligence is a field of computer science",
    "Machine Learning is a subset of AI",
    "FastAPI is used to build APIs",
    "Python is a programming language"
]

bm25 = BM25Retriever(docs)

dense = FakeDenseRetriever()

hybrid = HybridRetriever(
    dense,
    bm25
)

results = hybrid.retrieve(
    "FastAPI API",
    top_k=3
)

print(results)