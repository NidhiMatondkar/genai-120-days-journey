Employees = []

n =int(input("Enter no of employees:-"))
for i in range(n):
    emp_name = input("Enter Name of employee:-").strip()
    salary   = int(input("Enter salary :-"))
    
    if salary >=  100000:
         Bonus = "20%"
    elif salary >= 70000:
         Bonus = "10%"
    elif salary >= 40000:
         Bonus = "5%"
    else :
         Bonus = "0%"

         

    employee ={"Name" : emp_name,
               "Salary": salary,
               "Bonus" : Bonus
               }
    Employees.append(employee)
print("\n-----All the names of employees")
for employee in Employees:
     print(f"Name: {employee['Name']} | Salary: {employee['Salary']} |  Bonus: {employee['Bonus']}")