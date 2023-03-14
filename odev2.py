studentList = []
 
def addStudent():
    studentName = input("Enter your full name: ")
    studentList.append(studentName)

def removeStudent():
    studentName = input("Enter your full name: ")
    studentList.remove(studentName)

def addMultipleStudent():
    while studentList != "0":
        studentName = input("Enter student's full name: ")
        if studentName != "0":
            studentList.append(studentName)
            break
    print(studentList)

def listStudents():
    for student in studentList:
        print(student)
     
def studentNumber():
    student = input("Enter student name to find number: ")
    for i in range(len(studentList)):
      if studentList[i] == student: 
        print(i)

def removeMultipleStudent():
     while studentList != "0":
        studentName = input("Enter student's full name: ")
        if studentName != "0":
            studentList.remove(studentName)
            break
     print(studentList)

print("#########################")   
print("Adding a student")
addStudent()

print("#########################")   
print("Remove a student")
removeStudent()

print("#########################")   
print("Adding multiple students")
addMultipleStudent()

print("#########################")   
print("Student list")
listStudents()

print("#########################")   
print("Student Number")
studentNumber()

print("#########################")   
print("Delete multiple students")
removeMultipleStudent()