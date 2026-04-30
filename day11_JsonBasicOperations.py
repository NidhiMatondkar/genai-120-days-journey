import json

name = input("Enter Your name").strip()
age  = int(input("Enter Your age"))
goal = input("Enter your goal").strip()

person ={"name": name,
         "age": age,
         "goal": goal
}

with open("user.json","w") as file:
    json.dump(person,file)

with open("user.json","r") as file:
    data = json.load(file)
    print(data)