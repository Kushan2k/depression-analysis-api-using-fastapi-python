
from fastapi import FastAP
import random

#routers
from routers import chat_route
from routers import user_router

app = FastAPI(
    debug=True,
    title="Chat API",
    description="API for chat application",
    version="1.0.0",
)

@app.get('/')
async def index():
    """
    Root endpoint.
    """
    return {"message": "Welcome to the Chat API!"}

# routes definitions 
app.include_router(chat_route.router)
app.include_router(user_router.router)
