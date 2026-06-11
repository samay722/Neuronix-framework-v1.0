from neuronix.retriever.bm25_retriever import BM25Retriever

documents = [
"Artificial Intelligence is a field of computer science",
"Machine Learning is a subset of AI",
"FastAPI is used to build APIs",
"Python is a programming language"
]

retriever = BM25Retriever(documents)

results = retriever.retrieve(
"FastAPI API",
top_k=2
)

print(results)
