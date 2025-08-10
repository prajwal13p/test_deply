from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    name:str
    age:int

users = {
    1:{"name":"John", 'age':30},
    2:{'name':"Jane", 'age':20},
    3:{'name':"Jack", 'age':40}
}

@app.put("/users/{id}")
def update_user(id: int, user: user):
    if id in users:
        users[id] = user.model_dump()
        print(users)
        return {"message": "User updated successfully"}
    else:
        return {"message": "User not found"}

@app.get("/")
def root():
    return {"message": "Hello World"}

