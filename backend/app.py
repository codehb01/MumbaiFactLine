from flask import Flask, request
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse
from coordinator import run_pipeline   # <-- add this import
import os

load_dotenv()

app = Flask(__name__)

@app.route("/health")
def health():
    return "OK"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    from_number = request.values.get("From", "")

    print("Incoming WhatsApp message:", incoming_msg, "from", from_number)

    resp = MessagingResponse()
    reply = resp.message()

    # Call pipeline (Dev 2 + Dev 3 will improve this later)
    result_text = run_pipeline(incoming_msg)
    reply.body(result_text)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
