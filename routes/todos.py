import sys
sys.path.append('..')
from fastapi import APIRouter, Depends, HTTPException
from models import Base, Todos
from pydantic import BaseModel, Field
from database import Session_Local, engine
from sqlalchemy.orm import Session, session


Base.metadata.create_all(bind=engine)
def get_db():
    try:
        db = Session_Local()
        yield db
    except:
        db.close()

router =  APIRouter(prefix='/todos',tags=['todos'],responses={404:{'description':"Not Found"}})

class TodoModel(BaseModel):
    title: str
    description : str
    priority : int =  Field(gt=0,lt=6,description="Priority must be between 1-5")
    completed : bool


@router.get('/')
async def get_todos(db:session = Depends(get_db)):
    return db.query(Todos).all()

@router.post('/create_todo')
async def create_todos(todo:TodoModel,db:session = Depends(get_db)):
    todo_model = Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.completed = todo.completed
    db.add(todo_model)
    db.commit()
    return Successful_Response(201)

@router.delete('/delete_todo/{todo_id}')
async def delete_todos(todo_id:int,db:session = Depends(get_db)):
    todo_model = db.query(Todos).filter(Todos.id==todo_id).first()
    if todo_model is None:
        raise HTTP_Exception()
    db.query(Todos).filter(Todos.id==todo_id).delete()
    db.commit()
    return Successful_Response(201)

@router.put('/{todo_id}')
async def update_todos(todo_id:int,todo:TodoModel,db:session = Depends(get_db)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTP_Exception()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.completed = todo.completed
    db.add(todo_model)
    db.commit()
    return Successful_Response(200)

@router.patch('/{todo_id}')
async def update_status_todos(todo_id:int, completed:bool, db:session = Depends(get_db)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTP_Exception()

    todo_model.completed = completed
    db.add(todo_model)
    db.commit()
    return Successful_Response(200)

def Successful_Response(status_code:int):
    
    return {'status':status_code,'transaction':'Successfull'}

def Failed_Response(status_code:int):
    return {'status':status_code, 'transaction':"Failed"}

def HTTP_Exception():
    return HTTPException(status_code=404,detail='todo not found')