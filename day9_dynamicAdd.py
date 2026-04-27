def add_user():
    name = input("Enter user name:-").strip()
    age  = int(input("Enter user age:-"))
    goal = input("Enter your goal:-").strip()

    person ={"name":name,
              "age":age,
              "goal":goal
              }
    return person
people=[]
while True:
    choice = input("Enter your choice yes/no ?").lower().strip()
    if choice == "yes":
        user = add_user()
        if user["age"] >= 20:
         people.append(user)
        else:
            print("I can't add user ")
    elif choice == "no":
        break
    
        

print("\n--- All Users ---")
for person in people:
    print(person)