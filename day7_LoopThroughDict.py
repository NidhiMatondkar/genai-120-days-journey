name = input("Enter your name")
goal = input("Enter your goal")
age  = int(input("Enter your goal"))

person ={"name" : name,
         "goal":goal,
         "age":age}
for key,value in person.items():
    print(key,value)