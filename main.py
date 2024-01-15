from fastapi import FastAPI
from routes import todos
from routes import auth
import uvicorn


app =  FastAPI()
@app.get('/')
def page():
    return "Welcome to TODO APP"
app.include_router(todos.router)
app.include_router(auth.router)
config = uvicorn.Config("main:app", port=5000, log_level="info")
server = uvicorn.Server(config)

if __name__ == "__main__":
    server.run()
    