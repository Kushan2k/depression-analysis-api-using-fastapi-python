
from fastapi import FastAPI

#routers
from api.routers import user_router
from api.routers import chat_route

    
app = FastAPI(
    debug=True,
    title="Chat API",
    description="API for chat application",
    version="1.0.0",
    
)

# routes definitions 
app.include_router(user_router.router)
app.include_router(chat_route.router)
