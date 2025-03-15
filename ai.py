import os
from openai import OpenAI

class AIResponder:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, message: str) -> str:
        try:
            prompt = f'''
            You are responding to a text message.
            Keep your response short and concise as if you were texting (because you are).
            The user is asking: "{message}"
            Your response should be informative and relevant to the user's question.
            Avoid unnecessary details and keep the tone friendly.
            '''

            response = self.client.chat.completions.create(
                model="gpt-4o",  # Using "gpt-4o" as specified
                messages=[{"role": "user", "content": message}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error generating response: {str(e)}"