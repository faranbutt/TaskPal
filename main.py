from fastapi import FastAPI

from routes import todos
from routes import auth

app =  FastAPI()

app.include_router(todos.router)
app.include_router(auth.router)