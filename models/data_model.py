

from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str


class UserAnswers(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str
    q1_ans:str
