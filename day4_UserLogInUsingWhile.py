username = "Nidhi"
password = 1818
while True:
    user = input("Enter your username")
    user_pass = int(input("Enter password"))
    if username == user and password == user_pass:
        print("Login succssesful")
        break
    else:
        print("invalid username or password")
        