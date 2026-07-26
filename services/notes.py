from services.groq_service import GroqService


class NotesService:

    @staticmethod
    def generate_notes(text):

        prompt = f"""
You are an expert study assistant.

Convert the following document into structured study notes.

Requirements:

• Use proper headings
• Use bullet points
• Include important definitions
• Highlight key concepts
• Mention formulas (if present)
• Mention examples
• Mention important interview points
• Keep the notes concise and easy to revise
• Do NOT invent information.

Document:

{text}
"""

        return GroqService.generate(prompt)