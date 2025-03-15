# SMS-AI

A simple service that integrates Twilio SMS with OpenAI's GPT-4o model to respond to text messages with AI-generated replies.

## Features

- Receive SMS messages via Twilio webhook
- Process messages with OpenAI's GPT-4o model
- Send AI-generated responses back to the sender
- Containerized with Docker for easy deployment

## Prerequisites

- Python 3.9+
- Twilio account and phone number
- OpenAI API key
- Docker (optional, for containerization)

## Installation

1. Clone this repository
2. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the server:
   ```bash
   uvicorn main:app --reload
   ```
   
2. Configure your Twilio phone number webhook to point to your server's `/sms` endpoint.

3. Send a text message to your Twilio phone number and receive an AI-generated response.

## Docker Deployment

Build and run the Docker container:

```bash
docker build -t sms-ai .
docker run -p 8000:8000 -e OPENAI_API_KEY=your_openai_api_key sms-ai
```

## Configuration

- The AI model can be configured in the `ai.py` file
- Customize the prompt template in `generate_response` method to change how the AI responds

## License

This project is licensed under the MIT License - see the LICENSE file for details.
