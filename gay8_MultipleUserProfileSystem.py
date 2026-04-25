people = []
user = int(input("Enter the no of users"))
for i in range(user):
     name = input("Enter your Name")
     age  = int(input("Enter your age"))
     goal = input("Enter your Goal")
     person = {"name":name,
               "age":age,
               "goal":goal}  
     people.append(person) 
print("--- All Users ---")
for person in people:
          print("Name:", person["name"], "Age:", person["age"], "Goal:", person["goal"])
