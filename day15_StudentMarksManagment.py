students =[]

n = int(input("Enter no of student"))

for i in range(n):
    name = input("Enter student name:").strip()
    marks= int(input("Enter marks:"))

    if marks >= 90:
         grade = "A+"

    elif marks >= 75:
         grade = "A"

    elif marks >= 60:
         grade = "B"

    elif marks >= 35:
         grade = "E"

    elif marks <= 34:
         grade = "Fail"
  
    student={ "Name":name,
          "Marks":marks,
          "Grade":grade
     }
    
    students.append(student)
print("\n All the student List:")
for student in students:
      print(f"Name: {student['Name']} | Marks: {student['Marks']} | Grade: {student['Grade']}")

found = False
name = input("Enter user name:")
for student in students:
     
     if student["Name"] == name:
         print("-----User found----")
         print(f"Name: {student['Name']} | Marks: {student['Marks']} | Grade: {student['Grade']}")
         found = True
         break
if not found:
          print("Not found")

topper =students[0]
for student in students:
     if student["Marks"] > topper["Marks"]:
          topper = student
print("\n Topper of this year")
print(f"Name: {topper['Name']} | Marks: {topper['Marks']} | Grade: {topper['Grade']}")


name_del = input("Enter name to delete :").strip()
found = False
for student in students:
     if student["Name"] == name_del:
          students.remove(student)
          print("Student deleted")
          found = True
          break
if not found:
      print("Name not foun")
print("\n----Updated student List-----")
for student in students:
          print(f"Name: {student['Name']} | Marks: {student['Marks']} | Grade: {student['Grade']}")









