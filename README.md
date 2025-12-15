# Realtime AI Backend (WebSockets + Supabase)

## Overview
This project implements a high-performance asynchronous backend simulating a real-time conversational AI session using WebSockets, LLM streaming, and Supabase persistence.

## Tech Stack
- FastAPI
- WebSockets
- Supabase (Postgres)
- Async Python

## Setup Instructions
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app
