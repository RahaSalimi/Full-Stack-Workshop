
students_Dict={}
addStudnt = 'yes'

while addStudnt == 'yes':
    name = input('Please enter the name of the student: ')
    grade = int(input('Please enter the grade of the student: '))
    

    students_Dict[name] = [grade ]

    addContact = input('Would you like to add another student? (yes or no): ')

    if addContact == 'no':
        break

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
        new_grade=int(input())
        students_Dict.update({key:new_grade})
        print("grade updated =", new_grade)
    else:
        print("Student Not Exist")

    addupdate= input('Would you like to update another grade? (yes or no): ')
    if addupdate =='no':
        break
   


#function to delete a students
isdelete='yes'
def delete_grade():
  while isdelete== 'yes':
    remove_key= input("please enter student name to delete: ")
    if remove_key in students_Dict.keys():
	    pop_item = students_Dict.pop(remove_key)
        print("student {} removed from list",remove_key )
    else:
        print("Student Not Exist")

    adddelete= input('Would you like to update another grade? (yes or no): ')
    if adddelete =='no':
        break

action=input("what action do you want to take? (search  or update or delete): ")

if action == "search":
    search_grade()
elif action == "update":
    update_grade()




