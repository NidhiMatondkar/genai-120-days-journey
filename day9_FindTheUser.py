
people = [
    {"name": "Nidhi", "age": 23, "goal": "GenAI"},
    {"name": "Amit", "age": 26, "goal": "Design"},
    {"name": "Ankit", "age": 13, "goal": "CA"}
]

found = False 
find_name = input("Enter User name")

for person in people:
    if person["name"] == find_name:
        print(" user found: " ,person["name"],person["age"],person["goal"])
        found = True
        
if not found:
        print("user not found ")


   