def Login_System():
    user_name = "Nidhi"
    password  = 123455
    attempts  = 0
    
    while (True) :
        name  = input("username :-")
        passw = int(input("password:"))
        
       

        if  name == user_name  and passw == password:
            print("Login in successfully")
            break

        else:
              attempts = attempts + 1 
              print("Invalid username or password")

              if attempts >= 3:
                   print("Account blocked")
                   break

              
        


Login_System()