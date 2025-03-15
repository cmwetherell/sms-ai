import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file for local development

from fastapi import FastAPI, Form, Response
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from ai import AIResponder

app = FastAPI()
ai_responder = AIResponder()  # Initialize once when the app starts

@app.post("/sms")
async def sms_reply(Body: str = Form(...), From: str = Form(...)):
    incoming_msg = Body.strip()
    sender_number = From

    # Generate a response using the AIResponder
    reply_msg = ai_responder.generate_response(incoming_msg)

    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=reply_msg,
        from_="+19409783530",
        to=sender_number,
    )

    # print(message.body)

    # Create a TwiML response for Twilio
    resp = MessagingResponse()
    resp.message(reply_msg)

    return Response(content=str(resp), media_type="application/xml")


