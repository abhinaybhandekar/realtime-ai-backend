async def stream_response(prompt: str):
    response = f"AI response to: {prompt}"
    for word in response.split():
        yield word + " "
