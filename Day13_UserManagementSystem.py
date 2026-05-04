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

print("\n---USer Age >= 23----")
for person in user:
   if person["Age"] >= 23:
    print("name:", person["Name"] , "age:", person["Age"], "goal:" , person["Role"])
   
    
with open("userDetalis.json" , "w")as file:
   json.dump(user,file)


name_del = input("Enter name to delete:").strip().lower()
for person in user:
    if person["Name"].lower() == name_del:
        user.remove(person)
        break
        
print("\nAfter Deleting the user")
for person in user:
     print(f"Name: {person['Name']} | Age: {person['Age']} | Role: {person['Role']}")


edit_name = input("Enter name to edit: ").strip().lower()

found = False

for person in user:
    if person["Name"].lower() == edit_name:
        new_age = int(input("Enter new age: "))
        new_role = input("Enter new role: ").strip()

        person["Age"] = new_age
        person["Role"] = new_role

        print("User updated")
        found = True
        break   # ✅ important

if not found:
    print("User not found")

print("\nAfter editing:")

for person in user:
    print(f"Name: {person['Name']} | Age: {person['Age']} | Role: {person['Role']}")
    

     
    
     
