username = "Nidhi"
password = 1881

attempts = 0

while attempts < 3:
    user = input("Enter username: ")
    user_pass = int(input("Enter password: "))

    if user == username and user_pass == password:
        print("Login successful")
        break
    else:
        print("Wrong credentials")
        attempts = attempts + 1

if attempts == 3:
    print("Access denied")