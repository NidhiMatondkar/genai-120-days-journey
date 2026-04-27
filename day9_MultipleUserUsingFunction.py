def add_user():
    name = input("Enter user name").strip()
    age  = int(input("Enter user age"))
    goal = input("Enter user's goal").strip()

    person ={"name":name,
             "age":age,
             "goal":goal

    }
    return person

people = []
n = int(input("enter no of users"))

for i in range(n):
    user = add_user()
    people.append(user)
print(people)