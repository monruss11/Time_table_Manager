from sqlalchemy import Column, Integer, String, ForeignKey, Date
from datetime import date
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship, mapped_column
from sqlalchemy import create_engine
from typing import List

class Base(DeclarativeBase): pass
# Base=declarative_base()

class Student(Base):
    __tablename__='tbl_students'
    id=mapped_column('id', Integer, primary_key=True, index=True)
    name=mapped_column('name', String)
    family=mapped_column('family', String)
    nickname=mapped_column('nickname', String)
    lessons_rel=relationship("Lessons", back_populates='students_rel',\
                             cascade="all, delete-orphan")
    def __init__(self, name, family, nickname):
        self.name=name
        self.family=family
        self.nickname=nickname
        # telephone: str
        # mentor: bool
        # avatar: object
    def __repr__(self):
        return f'({self.id},{self.name},{self.family},{self.nickname})'

class Lessons(Base):
    __tablename__='tbl_lessons'
    id=mapped_column('id', Integer, primary_key=True, index=True)
    description=mapped_column('name', String)
    date=mapped_column('date', Date)
    student_id=mapped_column(Integer, ForeignKey('tbl_students.id'))
    students_rel=relationship('Student', back_populates='lessons_rel')

    def __init__(self, description, date, id_student ):
        self.description=description
        self.date=date
        self.student_id=id_student
    def __repr__(self):
        return f'({self.id}, {self.description}, {self.date}, {self.student_id})'

database='myh11.db'
engine=create_engine(f'sqlite:///{database}')
connection=engine.connect()

Base.metadata.create_all(bind=engine)
Session=sessionmaker(bind=engine)
session=Session(autoflush=False)





