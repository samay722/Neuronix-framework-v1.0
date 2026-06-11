class QueryRewriter:

    def __init__(self, llm):
        self.llm = llm

    def rewrite(self, query: str) -> str:

        prompt = f"""Rewrite the user query into a short search query
for a retrieval system.

Rules:
- Keep it SHORT (max 12-15 words)
- NO SQL
- NO explanations
- NO formatting
- ONLY keywords
- Preserve meaning

User query:
{query}

Rewritten query:
"""

        return self.llm.generate(prompt).strip()