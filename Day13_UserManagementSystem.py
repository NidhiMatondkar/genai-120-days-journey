import json
user = []
found = False

n = int(input("Enter no of users:"))

for i in range(n):
     name = input("Enter user name:").strip()
     age  = int(input("Enter user age:"))
     role = input("Enter user role:").strip()

     persons ={ "Name":name,
         "Age":age,
         "Role":role
         }
     
     user.append(persons)

print(user)

for person in user:
     print("name:", person["Name"] , "age:", person["Age"], "goal:" , person["Role"])


name = input("Search the name:").strip()
for person in user:
    if person["Name"] == name:
       print("name:", person["Name"] , "age:", person["Age"], "goal:" , person["Role"])
       found = True
       break

if not found:
    print("Not found the user")

print("---USer Age >= 23----")
for person in user:
    person["Age"] >= 23
    print("name:", person["Name"] , "age:", person["Age"], "goal:" , person["Role"])
    
with open("userDetalis.json" , "w")as file:
   json.dump(user,file)
    
     
