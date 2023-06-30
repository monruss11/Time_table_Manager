from fastapi import FastAPI, Form, File, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
import uvicorn
import os
from typing import Optional, Dict
from schemas import session as db
from schemas import Student, Lessons
import read_write_module as rw

app = FastAPI()
path = os.path.dirname(__file__)
templates = Jinja2Templates(directory=f'{path}/templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    data_page = {'title': 'Start page'}
    return templates.TemplateResponse('start_page.html', {'request': request, 'data_page': data_page})


@app.post('/manage', response_class=HTMLResponse)
async def res(request: Request, access: Optional[str] = Form(None)):
    data_page = {'title': access, 'col_count': 0}
    if access == None:
        app.post('/', response_class=HTMLResponse)
        data_page['title'] = 'You need choice access level'
        return templates.TemplateResponse('start_page.html', \
                                          {'request': request, 'data_page': data_page})
    if access == "Student":
        data_page['title'] = 'Manage Student'
        return templates.TemplateResponse('student_operation.html', \
                                          {'request': request, 'data_page': data_page})

# @app.post('/student/add', response_class=HTMLResponse)
# async def res(request: Request, operation: Optional[str] = Form(None)):


@app.post('/student', response_class=HTMLResponse)
async def res(request: Request, operation: Optional[str] = Form(None)):
    if operation == "Edit Student":
        data_page = {'title': 'Choice Student for Edit', 'action': 'choice'}
        return templates.TemplateResponse('edit_student_page.html',
                                          {'request': request, 'data_page': data_page})
    if operation == "Add Student":
        data_page = {'title': 'Add Student', 'action': 'add'}
        return templates.TemplateResponse('add_stud_page.html',
                                          {'request': request, 'data_page': data_page})

@app.post('/student/edit', response_class=HTMLResponse)
def choice_student(request: Request, std_id:Optional[int]=Form(None),
                std_name: Optional[str] = Form(None),
                std_family: Optional[str] = Form(None),
                std_nickname: Optional[str] = Form(None),
                std_telephone: Optional[str] = Form(None),
                std_login: Optional[str] = Form(None), std_password: Optional[str] = Form(None)
                ):
    # student=Student()
    global student
    if std_id!=None:
        student = db.query(Student).filter(Student.id==std_id).first()
        # db.add(student); db.commit()
    data_page = {'title': 'Edit Student', 'student': student,'action':'edit'}
    return templates.TemplateResponse('edit_student_page.html', {'request': request, 'data_page': data_page})

@app.post('/student/update', response_class=HTMLResponse)
def edit_student(request: Request, std_id:Optional[int] = Form(None),
                std_name: Optional[str] = Form(None),
                std_family: Optional[str] = Form(None),
                std_nickname: Optional[str] = Form(None),
                std_telephone: Optional[str] = Form(None),
                std_login: Optional[str] = Form(None), std_password: Optional[str] = Form(None)
                ):
    # student=Student()
    global student
    student.id = std_id
    student.name = std_name; student.family = std_family; student.nickname = std_nickname
    student.telephone = std_telephone; student.login = std_login; student.password = std_password
    db.commit()
    data_page = {'title': 'Updated Student Data', 'student': student,'action':'edit'}
    return templates.TemplateResponse('edit_student_page.html',
                                      {'request': request, 'data_page': data_page})


@app.post('/student1', response_class=HTMLResponse)
def new_student(request: Request, std_id:Optional[int]=Form(None),
                std_name: Optional[str] = Form(None),
                std_family: Optional[str] = Form(None),
                std_nickname: Optional[str] = Form(None),
                std_telephone: Optional[str] = Form(None),
                std_login: Optional[str] = Form(None), std_password: Optional[str] = Form(None)
                ):
    student=Student()

    # student.id=std_id
    student.name = std_name; student.family = std_family; student.nickname = std_nickname
    student.telephone=std_telephone; student.login=std_login; student.password=std_password
    db.add(student)
    db.commit()
    data_page = {'title': 'Yes', 'student': student}
    return templates.TemplateResponse('edit_student_page.html', \
                                      {'request': request, 'data_page': data_page})

# ==================Main===============================
if __name__ == '__main__':
    r_w = rw
    student=Student()
    uvicorn.run('main:app', reload=True, port=8080)
