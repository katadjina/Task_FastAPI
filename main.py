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

#get one
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for item in todos:
        if item.id == todo_id:
            return {"todo" : item}
    return {"message": "no todo found"}


#create new with POST method
@app.post("/todos")
#pass a todo item of a type ToDo(model)
async def create_todos(todo: ToDo):
    #add to the list 
    todos.append(todo)
    return {"message": "ToDo has been added"}

#update  -> PUT method
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo_obj: ToDo):
    for item in todos:
        if item.id == todo_id:
            item.id = todo_obj.id
            item.item = todo_obj.item    
            return {"todo" : item}
    return {"message": "no todo with this id has was found"}



#delete one
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for item in todos:
        if item.id == todo_id:
            todos.remove(item)
            return {"message" : "Todo has been removed"}
    return {"message": "no todo found"}


#swagger and reDoc built in -> in a browser: localhost:8000/docs (or redoc)
