Pepole = []
with open ("UserDetails.csv" , "r") as file:
     lines = file.readlines()
     print(lines)
     for line in lines:
         part = line.strip().split(",")
         name = part[0]
         age  = part[1]
         goal = part[2]
           
         person ={ "name":part[0],
                   "age":int(part[1]),
                   "goal":part[2]
                    }
          
         Pepole.append(person)
         print(Pepole)
    

