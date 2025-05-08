from typing import Union
from pydantic import BaseModel


class ChatRequestBody(BaseModel):
    """
    Request body for chat completion.
    """

    q_no:int
    answer:Union[int, float,str]
