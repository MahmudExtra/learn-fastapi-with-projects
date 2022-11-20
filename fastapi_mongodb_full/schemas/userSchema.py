def userEntity(item):
    return {
        "_id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }
# from schemas.userSchema import userEntity, usersEntity



def usersEntity(entity) -> list:
    # return list(map(lambda item: userEntity(item), entity))
    # return [userEntity(item) for item in entity]
    return  list(map(userEntity, entity))
        


