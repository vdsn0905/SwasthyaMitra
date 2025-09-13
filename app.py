import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
from bot.chatbot import health_chatbot

load_dotenv()

app = Flask(__name__)

@app.route("/sms", methods=['POST'])
def sms_reply():
    user_msg = request.form.get('Body')
    reply_text = health_chatbot(user_msg)
    response = MessagingResponse()
    response.message(reply_text)
    return str(response)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)

