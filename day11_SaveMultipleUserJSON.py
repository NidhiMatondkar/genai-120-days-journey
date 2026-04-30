import json 
people=[]

n = int(input("Enter no of users:"))

for i in range(n):

    name = input("Enter user name:").strip()
    age  = int(input("Enter your age"))
    goal = input("Enter your goal").strip()

    person = { "name": name,
               "age": age,
               "goal":goal
               }
    people.append(person)
print(people)

with open("MultiUser.json","w") as file:
     json.dump(people,file)


