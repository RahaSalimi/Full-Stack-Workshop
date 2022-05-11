
students_Dict={}

addStudnt = 'yes'
# function to add student
def add_student():
 while addStudnt == 'yes':
    name = input('Please enter the name of the student: ')
    grade = int(input('Please enter the grade of the student: '))
    

    students_Dict[name] = [grade ]

    addContact = input('Would you like to add another student? (yes or no): ')

    if addContact == 'no':
        return students_Dict

# function to search a student
issearch='yes'
def search_grade():
    while issearch == 'yes':
        search_grade = int(input("plese enter a grade to search: "))
        for name, grade in students_Dict.items():  
          if grade == search_grade:
            print("we found the a student with name of " + name + " for grade: "  + grade)
          else:
            print("sorry we couldnt find the grade in  list. please try another grade")   

        addsarch= input('Would you like to search another grade? (yes or no): ')
        if addsarch == 'no':
         break


#function to update a student's grade
isupdate ='yes'
def update_grade():
  while isupdate =='yes':
    key = input("please enter student name to update: ")
    if key in students_Dict.keys():
        print("student exist,please enter new grade ")
        new_grade=int(input("enter new grade: "))
        students_Dict.update({key:new_grade})
        print("grade updated to: ", new_grade)

    else:
        print("Student Not Exist")

    addupdate= input('Would you like to update another grade? (yes or no): ')
    if addupdate =='no':
        return students_Dict
 
   

#function to delete a students
def delete_grade():
    remove_key=input ("enter the name of the student you want to delete")
    if remove_key in students_Dict.keys():
        students_Dict.pop(remove_key)
        print("student {} has been deleted", remove_key)
    else:
        print("name not found")
        
    return students_Dict

action=input("what action do you want to take? (add , search  , update or delete): ")

if action == "add":
     add_student()
elif action == "search":
    search_grade()
elif action == "update":
    update_grade()
elif action =="delete":
    delete_grade()



