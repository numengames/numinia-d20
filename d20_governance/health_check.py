# health_check.py

import uvicorn
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/health")
async def health_check():
    return Response(status_code=200)

async def start_server():
    config = uvicorn.Config(app=app, host="0.0.0.0", port=8000, loop="asyncio")
    server = uvicorn.Server(config)
    await server.serve()
