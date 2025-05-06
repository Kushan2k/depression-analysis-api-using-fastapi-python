
from typing import Union

from fastapi import FastAPI
from models.models import UserData

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/predict')
async def predict(data: UserData):
    """
    Predict the user data.
    """
    # Here you would typically call your model to make a prediction
    # For demonstration purposes, we'll just return the data back
    return {
        "id": data.id,
        "name": data.name,
        "email": data.email,
        "password": data.password,
        
    }
