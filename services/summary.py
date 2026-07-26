from services.groq_service import GroqService


class SummaryService:

    @staticmethod
    def generate_summary(text):

        prompt = f"""
You are an expert document summarizer.

Summarize the following document.

Requirements:

- Professional tone
- Use headings
- Bullet points
- Mention important definitions
- Mention key concepts
- Mention conclusions
- Maximum 500 words

Document:

{text}
"""

        return GroqService.generate(prompt)