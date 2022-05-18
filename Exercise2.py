
# function to add student
from turtle import update


def add_student():
    name = input('Please enter the name of the student: ')
    grade = int(input('Please enter the grade of the student: '))
    students_Dict[name] = [grade ]
    addContact = input('Would you like to add another student? (yes or no): ')
    if addContact == 'yes':
      add_student()
    else:
     return students_Dict


# function to search a student

def search_student():
    
        name = input("plese enter name of student: ")
        if name in students_Dict.keys():  
            print("we found a student with name of " , name ," with grade"  , students_Dict[name])
        else:
            print("sorry we couldnt find the grade in  list. please try another grade")   
            
        addsarch= input('Would you like to search another grade? (yes or no): ')
        if addsarch == 'yes':
         search_student(students_Dict)

        else:
          return students_Dict
    


#function to update a student's grade

def update_student():
  
    name = input("please enter student name to update: ")
    if name in students_Dict.keys():
      choices= input("what field do you want to update ? (name or grade) : ")
      if choices== "name":
        grade=students_Dict[name]
        new_name=input("enter new name: ")
        students_Dict.pop(name)
        students_Dict[new_name]=grade
        print("name successfully updated to: ", new_name)
      elif choices== "grade":
        new_grade=input("enter new grade: ")
        students_Dict[name]=new_grade

    else:
        print("Student Not Exist")

    addupdate= input('Would you like to update more? (yes or no): ')
    if addupdate =='yes':
      update(students_Dict)
    else:
        return students_Dict
 
   

#function to delete a students
def delete_student():
    remove_key=input ("enter the name of the student you want to delete: ")
    if remove_key in students_Dict.keys():
        students_Dict.pop(remove_key)
        print("student ", remove_key,"has been deleted")
        print(students_Dict)
    else:
        print("name not found")
        
    return students_Dict

students_Dict={}
while(1):
  action=input("what action do you want to take? (add , search  , update or delete): ")
  if action == "add":
     add_student()
     print(students_Dict)
  elif action == "search":
    search_student()
  elif action == "update":
    update_student()
  elif action =="delete":
    delete_student()



