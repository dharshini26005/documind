from services.groq_service import GroqService


class FlowchartService:

    @staticmethod
    def generate_flowchart(text):

        prompt = f"""
You are an expert document analyst.

Analyze the document carefully and convert it into a Mermaid Flowchart.

Rules:

1. Return ONLY Mermaid syntax.
2. Do NOT explain anything.
3. Start with:

graph TD

4. Show the relationship between concepts.
5. Keep it clean and readable.

Document:

{text}
"""

        return GroqService.generate(prompt)