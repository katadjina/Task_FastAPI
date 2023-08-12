from fastapi import FastAPI
from pydantic import BaseModel


class ToDo(BaseModel):
    name: str
    description: str 
        