from services.groq_service import GroqService


class MindMapService:

    @staticmethod
    def generate_mindmap(text):

        prompt = f"""
You are an expert educational content organizer.

Convert the following document into a Mermaid Mind Map.

Rules:

1. Return ONLY Mermaid syntax.
2. Do NOT explain anything.
3. Do NOT use ``` or ```mermaid.
4. Start exactly with:

mindmap

5. Use a single root node.
6. Create meaningful parent-child relationships.
7. Keep labels short (2–5 words).

Example:

mindmap
  root((Machine Learning))
    Types
      Supervised
      Unsupervised
      Reinforcement
    Workflow
      Data Collection
      Data Cleaning
      Training
      Evaluation
      Deployment
    Applications
      Healthcare
      Finance
      E-Commerce

Document:

{text}
"""

        response = GroqService.generate(prompt)

        # Clean output
        response = response.replace("```mermaid", "")
        response = response.replace("```", "")
        response = response.strip()

        return response