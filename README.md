# Temple SaaS Full System

## Run Dashboard

streamlit run dashboard/app.py

## Run Webhook

uvicorn api.webhook:app --host 0.0.0.0 --port 10000
