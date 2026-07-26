from services.semantic import SemanticSearchService
from services.groq_service import GroqService


class RAGService:

    @staticmethod
    def ask(question):

        # Retrieve relevant chunks
        data = SemanticSearchService.search(question)

        if not data or "documents" not in data:
            return "No relevant information found."

        documents = data["documents"][0]

        context = "\n\n".join(documents)

        prompt = f"""
You are an AI assistant for DocuMind Studio.

Answer ONLY using the provided document context.

If the answer is not present in the context,
reply:

"I couldn't find this information in the uploaded document."

------------------------
DOCUMENT CONTEXT

{context}

------------------------

QUESTION

{question}

------------------------

Provide:

• Clear answer
• Professional explanation
• Bullet points if needed
• Do not make up information.
"""

        return GroqService.generate(prompt)