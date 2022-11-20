from fastapi import FastAPI
from routes.userRoute import user
app = FastAPI()


@app.get('/')
def home():
    return {'message': 'Hello World'}


app.include_router(user)
