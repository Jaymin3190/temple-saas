from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse
import json

app = FastAPI()

VERIFY_TOKEN = "temple_verify_token"

@app.get("/")
async def root():
    return {"status": "Webhook server running"}

@app.get("/webhook")
async def verify_webhook(request: Request):

    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge)

    return {"error": "Verification failed"}

@app.post("/webhook")
async def receive_webhook(request: Request):

    body = await request.json()

    print(json.dumps(body, indent=2))

    return {"success": True}
