from fastapi import APIRouter

from models.userModel import User
from bson import ObjectId
from config.databaseConfig import connection
from schemas.userSchema import usersEntity,userEntity


user = APIRouter()

# get all the users from mongodb database with objectid validation iteration


@user.get('/users')
async def get_users():
    return usersEntity(connection.test.users.find({}))


@user.get('/user/{id}')
async def get_users(id: str):
    return userEntity(connection.test.users.find_one({"_id": ObjectId(id)}))


@user.post("/user")
async def createUser(user: User):
    result = connection.test.users.insert_one(user.dict())
    return result.acknowledged


@user.put("/user/{id}")
async def updateUser(id: str, user: User):
    result = connection.test.users.update_one({"_id": ObjectId(id)}, {"$set":dict(user)})
    return result.acknowledged

@user.delete("/user/{id}")
async def deleteUser(id: str):
    result = connection.test.users.delete_one({"_id": ObjectId(id)})
    return result.acknowledged