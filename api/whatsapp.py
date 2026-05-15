import requests
import os

TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

URL = (
    f"https://graph.facebook.com/v22.0/"
    f"{PHONE_NUMBER_ID}/messages"
)

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def send_text_message(phone, message):

    payload = {
        "messaging_product": "whatsapp",
        "to": phone,
        "type": "text",
        "text": {
            "body": message
        }
    }

    response = requests.post(
        URL,
        headers=headers,
        json=payload
    )

    return response.json()
