name = input("Enter your Name")
age  = int(input("Enter your age"))
goal = input("Enter your goal")

person ={"name":name ,
         "age":age,
         "goal":goal}
print("-----User Profile-----")
print("Name:",person["name"])
print("Age:",person["age"])
print("Goal:",person["goal"])
