name = input("Enter you name").strip()
with open ("user.txt","a") as file:
    file.write(name +"\n")
     