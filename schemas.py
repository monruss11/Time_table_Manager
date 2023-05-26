from pydantic import BaseModel
from datetime import date

class Student(BaseModel):
    id: int
    name: str
    family: str=None
    nickname: str
    telephone: str
    login:str
    password:str
    mentor: bool
    avatar: object

class Calendar(BaseModel):
    id: int
    date: date
    description: str

class Homework(BaseModel):
    id: int
    work_descript: str






