
from typing import Union

from fastapi import FastAPI
from api.models.models import UserData

#routers
from api.routers import user_router
from api.routers import chat_route

app = FastAPI(
    debug=True,
    
    
)


app.include_router(user_router.router)

@app.get("/chat/test/{id}")
def read_root(id:int):
    return {"Hello": f"World {id}" }

app.include_router(chat_route.router)
