from fastapi import FastAPI
from pydantic import BaseModel


class ToDo(BaseModel):
    id: int
    item: str 
        