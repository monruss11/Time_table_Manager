from fastapi import FastAPI, Form, File, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from  fastapi import Request
import uvicorn
import os
from typing import Optional,Dict
from schemas import Student, Calendar, Homework
import read_write_module as rw

app=FastAPI()
path=os.path.dirname(__file__)
templates = Jinja2Templates(directory=f'{path}/templates')
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request ):
  global index; global check_count; global str_url; global url_googlesheet
  data_page = { 'title': 'Start page' }
  return templates.TemplateResponse('start_page.html', {'request': request, 'data_page': data_page})

@app.post('/student',response_class=HTMLResponse)
async def res(request: Request, access:Optional[str]=Form(None)):
  global check_count; global str_url; global row_count; global col_count

  data_page={ 'title':access, 'col_count':0 }
  if access==None:
    app.post('/',response_class=HTMLResponse)
    data_page['title']='You need choice access level'
    return templates.TemplateResponse('start_page.html',\
                        {'request': request, 'data_page': data_page})

  if access=="Student":
    data_page['title']='Manage Student'
    return templates.TemplateResponse('student_page.html',\
                        {'request': request, 'data_page': data_page})


@app.post('/student/add',response_class=HTMLResponse)
async def res(request: Request, operation:Optional[str]=Form(None)):
  global check_count; global str_url; global row_count; global col_count

  data_page={ 'title':operation, 'col_num':0, 'row_num':0 }
  if operation=="Add Student":
    data_page['title']='Add Student'
    return templates.TemplateResponse('add_stud_page.html',\
                        {'request': request, 'data_page': data_page})

@app.post('/student1', response_class=HTMLResponse)
def new_student(request: Request, std_name:Optional[str] = Form(None),std_family:Optional[str]= Form(None),\
                  std_nickname:Optional[str] = Form(None), std_telephone:Optional[int] = Form(None),
                  std_login:Optional[str] = Form(None), std_password:Optional[str] = Form(None)
                ):
  student=Student; global idn

  student.name=std_name;  student.family=std_family; student.nickname=std_nickname
  student.telephone=std_telephone; student.login=std_login; student.password=std_password
  # idn=idn+5
  # student.id=idn
  data_page = {'title':'Yes', 'student': student}
  return templates.TemplateResponse('student_page1.html', \
                                    {'request': request, 'data_page': data_page})


@app.post('/calendar', response_class=HTMLResponse)
def lesson_dates(std_calendar: Calendar):
  return std_calendar

# ==================Main===============================
if __name__=='__main__':
  index=[]; access=''; idn=0

  r_w=rw
  uvicorn.run('main:app', reload=True, port=8080)