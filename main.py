
from typing import Union

from fastapi import FastAPI
from api.models.models import UserData

#routers
from api.routers import user_router

app = FastAPI(
    debug=True,
    
)

app.include_router(
    user_router.router,
    prefix="/api/v1",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}
