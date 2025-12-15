import os
from dotenv import load_dotenv
from supabase import create_client
from datetime import datetime
from pathlib import Path

# 🔥 Force-load .env using absolute path (Windows-safe)
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

print("DEBUG ENV PATH:", ENV_PATH)
print("DEBUG SUPABASE_URL:", url)

if not url or not key:
    raise RuntimeError("Supabase env vars not loaded")

supabase = create_client(url, key)


async def start_session(session_id):
    supabase.table("sessions").insert({
        "session_id": session_id,
        "start_time": datetime.utcnow().isoformat()
    }).execute()


async def save_event(session_id, role, message):
    supabase.table("events").insert({
        "session_id": session_id,
        "role": role,
        "message": message
    }).execute()


async def end_session(session_id):
    supabase.table("sessions").update({
        "end_time": datetime.utcnow().isoformat()
    }).eq("session_id", session_id).execute()
