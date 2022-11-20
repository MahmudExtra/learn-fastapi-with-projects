from dataclasses import Field
import uuid
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str
  
