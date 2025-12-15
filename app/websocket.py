from fastapi import WebSocket
from app.llm import stream_response
from app.database import save_event, start_session, end_session
import asyncio

async def handle_ws(ws: WebSocket, session_id: str):
    await ws.accept()
    await start_session(session_id)

    try:
        while True:
            user_msg = await ws.receive_text()
            await save_event(session_id, "user", user_msg)

            async for token in stream_response(user_msg):
                await ws.send_text(token)
                await asyncio.sleep(0.05)

    except:
        await end_session(session_id)
