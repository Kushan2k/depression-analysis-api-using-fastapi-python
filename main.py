
from typing import Annotated, Union
from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI
from sqlalchemy.engine.base import Engine
from api.models.models import UserData
#routers
from api.routers import user_router
from api.routers import chat_route
from sqlmodel import  Session,  create_engine, select,SQLModel
from api.models.data_model import Hero

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine: Engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

model=None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    create_db_and_tables()
    
    yield
    # Clean up the ML models and release the resources
    


app = FastAPI(
    debug=True,
    lifespan=lifespan,
)


@app.post("/heroes")
def create_hero(hero: Hero, session: SessionDep) -> Hero:
    print("Req came")
    
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero



app.include_router(user_router.router)

@app.get("/chat/test/{id}")
def read_root(id:int):
    return {"Hello": f"World {id}" }

app.include_router(chat_route.router)
