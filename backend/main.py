from fastapi import FastAPI, HTTPException

from model import Todo

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

# an HTTP-specific exception class  to generate exception information

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:8000",
]

# what is a middleware? 
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "Future"}

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo/{nom}", response_model=Todo)
async def get_todo_by_title(nom):
    response = await fetch_one_todo(nom)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {nom}")

@app.post("/api/todo/", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")

@app.put("/api/todo/{nom}/", response_model=Todo)
async def put_todo(nom: str, Group: str):
    response = await update_todo(nom, Group)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {nom}")

@app.delete("/api/todo/{nom}")
async def delete_todo(nom):
    response = await remove_todo(nom)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {nom}")