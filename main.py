
from fastapi import FastAPI

#routers
from routers import chat_route
from routers import user_router

app = FastAPI(
    debug=True,
    title="Chat API",
    description="API for chat application",
    version="1.0.0",
)

# routes definitions 
app.include_router(chat_route.router)
app.include_router(user_router.router)
