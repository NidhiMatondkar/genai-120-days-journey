skill = ["ML" , "Python" ,"Agentic Ai" , "DS" , "DA"] 

#adding method
#method 1
skill.append("genAi") # adding the element at end
print(skill)

#method 2
skill.insert(0,"Ai")

#there are different types for removing elements in List
# method 1 pop() 
skill.pop(3) 

#method 2 remove()
skill.remove("DA")

#method 3 del()
del skill[0:3]
print(skill)