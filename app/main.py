from fastapi import FastAPI, WebSocket
from app.websocket import handle_ws

app = FastAPI()

@app.websocket("/ws/session/{session_id}")
async def websocket_endpoint(ws: WebSocket, session_id: str):
    await handle_ws(ws, session_id)
