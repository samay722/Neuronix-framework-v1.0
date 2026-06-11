from neuronix.reranker.bge_reranker import BGEReranker

docs = [
    "FastAPI is used to build APIs",
    "Python is a programming language",
    "Artificial Intelligence is a field of computer science"
]

reranker = BGEReranker()

results = reranker.rerank(
    query="FastAPI framework",
    documents=docs,
    top_k=2
)

print(results)