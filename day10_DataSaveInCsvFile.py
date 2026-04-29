name = input("Enter your name :").strip()
age  = int(input("Enter your age:"))
goal = input("Enter your goal:").strip()

with open("UserDetails.csv","a") as file:
   file.write(f"{name},{age},{goal}\n")
    