import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class GroqService:

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    @staticmethod
    def generate(prompt):

        response = GroqService.client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "system",
                    "content":
                    "You are an expert document analyst. "
                    "Always answer professionally."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3

        )

        return response.choices[0].message.content