from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import os
import json

app = FastAPI()

VERIFY_TOKEN = os.getenv(
    "VERIFY_TOKEN",
    "temple_verify_token"
)

@app.get("/")
async def home():
    return {
        "status": "Webhook server running"
    }

@app.get("/webhook")
async def verify_webhook(request: Request):

    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    print("Webhook verification request received")

    if mode == "subscribe" and token == VERIFY_TOKEN:

        print("Webhook verified")

        return PlainTextResponse(challenge)

    return PlainTextResponse(
        "Verification failed",
        status_code=403
    )

@app.post("/webhook")
async def receive_webhook(request: Request):

    body = await request.json()

    print(json.dumps(body, indent=2))

    return {"success": True}