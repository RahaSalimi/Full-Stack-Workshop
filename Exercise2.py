
students_Dict={}
addStudnt = 'yes'

while addStudnt == 'yes':
    name = input('Please enter the name of the student: ')
    grade = int(input('Please enter the grade of the student: '))
    

    students_Dict[name] = [grade ]

    addContact = input('Would you like to add another student? (yes or no): ')

    if addContact == 'no':
        break

#print (students_Dict)


issearch='yes'

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