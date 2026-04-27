def add_user():
     name = input("Enter user name").strip()
     age  = int(input("Enter your age"))
     goal = input("Enter you goal").strip()
     
     person ={ "name":name,
                "age":age,
                "goal":goal
                }
     return person 
user1 = add_user()
print("User1",user1)