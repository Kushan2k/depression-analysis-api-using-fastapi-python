from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    name: str
    email: str
    password: str
    

    