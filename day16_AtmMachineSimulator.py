def ATM_Machine():
    Balance = 200000
    
    while(True) :
        choice = int(input("Enter your choice"))
        if choice == 1:
           check_balance = Balance
           print("Current balance :-",check_balance)
           
        elif choice == 2:
            Deposite   = int(input("Enter amout to deposite:-"))
            Balance = Deposite + Balance
            print(Deposite," Amount is debited from your current account and balance is ", Balance)
            
        elif choice == 3:
            with_draw = int(input("Enter amount to withdraw:-"))
            if Balance >= with_draw:
               Balance = Balance - with_draw
               print(Balance , "Amount creadited from your bank")
            
        elif choice == 4 :
              print("Exit")              
              break
              
        else:
            print("wrong choice")
ATM_Machine()



            
    