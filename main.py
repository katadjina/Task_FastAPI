from fastapi import FastAPI
from models import ToDo


#create an instance of fastapi class
app = FastAPI()

# path decorator
@app.get("/")
#in fast api async is built in
async def root():
    #returns json
    return {"message": "Hello"}

#rune the server -> command: uvicorn main:app --reload
# open localhost or test on Postman by adding projets's local webserver port eg. localhost:8000

todos = []

#get all notes
@app.get("/todos")
async def get_todos():
    return {"todos": todos}


#create new with POST method
@app.post("/todos")
#pass a todo item of a type ToDo(model)
async def create_todos(todo: ToDo):
    #add to the list 
    todos.append(todo)
    return {"message": "ToDo has been added"}