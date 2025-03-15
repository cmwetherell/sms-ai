import os
from openai import OpenAI

# add a logger
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIResponder:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")
        self.client = OpenAI(api_key=api_key)

    def generate_response(self, message: str) -> str:
        try:
            # log the incoming message
            logger.info(f"Incoming message: {message}")

            prompt = f'''
            You are responding to a text message.
            Keep your response short and concise as if you were texting (because you are).
            The user is asking: "{message}"
            Your response should be informative and relevant to the user's question.
            Avoid unnecessary details and keep the tone friendly.
            '''

            response = self.client.responses.create(
                model="gpt-4o",
                tools=[{"type": "web_search_preview"}],
                input=prompt
            )

            # log response
            logger.info(f"AI response: {response}")
            
            return response.output_text
        except Exception as e:
            return f"Error generating response: {str(e)}"