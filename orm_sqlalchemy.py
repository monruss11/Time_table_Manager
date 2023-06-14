import datetime
# from schemas import * # Student, Base
import schemas as db


# Insert data to Student Table
stud1=db.Student('ffff','uuuuu','rrrr'); db.session.add(stud1)
stud2=db.Student('gtff','tquu','rdfgarrr'); db.session.add(stud2)
stud5=db.Student('nnn','mmmm','sssss'); db.session.add(stud5)
db.session.commit()

# Insert data to Lessons Table
assembler=db.Lessons('assembler', datetime.date(2023,6,11),stud2.id)
c_plus=db.Lessons('c++', datetime.date(2023,7,11), stud1.id)
c=db.Lessons('c', datetime.date(2023,6,15),stud2.id)
db.session.add(assembler); db.session.add(c_plus); db.session.add(c)
db.session.commit()

#More then one lessons for single student
stud_lessons=db.session.query(db.Lessons).filter(db.Lessons.student_id == 2).all()
print('Lessons for student id 2',stud_lessons,'\n')


result=db.session.query(db.Student).all()
print('Student List:',result,'\n')

# Update
stud7=db.session.query(db.Student).filter(db.Student.name=='ffff').first()
db.session.add(stud7); db.session.commit(); db.session.refresh(stud7)
stud7.name='TTTT'; db.session.commit()

# Delete student
stud = db.session.query(db.Student).filter(db.Student.name == "ffff").first()
if stud != None:
  db.session.delete(stud)
  db.session.commit()

result=db.session.query(db.Student).all()
lesson_result=db.session.query(db.Lessons).all()
print('Lessons', lesson_result,'\n')
print('New_student_list',result)


