from fastapi import APIRouter
from pydantic import BaseModel

class CreateUser(BaseModel):
    id:int
    username:str
    password:str    

router =  APIRouter(prefix='/auth',tags=['auth'],responses={200:{"description":"Create User"}})

@router.post('/signup')
async def signup(create_user:CreateUser):
    return {"message":f"my name is {create_user.username}"}

