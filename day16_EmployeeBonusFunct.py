def employee_Bonus(salary):
    if salary >=  100000:
         Bonus = "20%"
       
    elif salary >= 75000:
        Bonus = "10%"
        
    elif salary >= 50000:
        Bonus = "5%"
        
    else :
        Bonus = "0%"

    return Bonus
        
result = employee_Bonus(75000)
print(result)


    