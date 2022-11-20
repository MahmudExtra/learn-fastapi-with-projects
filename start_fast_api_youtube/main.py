import logging
from typing import List, Union
from uuid import UUID, uuid4
import logging
from fastapi.encoders import jsonable_encoder
from fastapi import FastAPI

from models import Gender, Role, User

app = FastAPI()

# now we are going to create a fake database
db: List[User] =[
    User(
        id="8601a971-25ef-4311-8edd-3ca248adfb4f",
        #id = UUID("8601a971-25ef-4311-8edd-3ca248adfb4f"),
        firstName='Mahmud',
        lastName='Qudtati',
        gender=Gender.male,
        roles=[Role.student]
        ),
    User(
        id="143c3e36-f0cf-4cf7-be71-109035a86086",
        #id = UUID("143c3e36-f0cf-4cf7-be71-109035a86086")
        firstName='Mahmudul',
        lastName='Haque',
        gender=Gender.male,
        roles=[Role.admin, Role.user]
        )
]
# logging.warning(enumerate(db))
#  make a foor loop for  db



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/api/users')
async def fetch_users():
    return db


@app.post("/api/users")
async def create_user(user: User):
    db.append(user)
    return user



@app.delete("/api/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    return {"message": "User not found"}

@app.put("/api/users/{user_id}")
async def update_user(user_id: UUID, user: User):
    update_item_encoded = jsonable_encoder(user)
    for index, user in enumerate(db):
        if user.id == user_id:
            db[index] = update_item_encoded
            return {"message": "User updated successfully"}
    return {"message": "User not found"}

