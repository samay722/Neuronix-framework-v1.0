from neuronix.query.rewriter import QueryRewriter
from neuronix.llm.groq_llm import GroqLLM


llm = GroqLLM()

rewriter = QueryRewriter(llm)

queries = [
    "What is it?",
    "How does it work?",
    "Explain FastAPI"
]

for q in queries:

    rewritten = rewriter.rewrite(q)

    print("\nOriginal:", q)
    print("Rewritten:", rewritten)