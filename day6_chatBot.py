def chatBot(user_input):
    user_input =user_input.strip().lower() #strip removes the extra space and lower will handdle letters
    

    #if "Hello" in user_input: this was not working because above I have used .lower() so it is missmatching
        #return "Hi there 👋"
    if "hello" in user_input:
        return "Hi there 👋"
    elif "name" in user_input:
        return "I am GenAI Bot 🤖"
    elif "skill" in user_input:
        return "You are learning python and genAi"
    elif "bye" in user_input:
        return "Good bye see you again"
    else:
        return "I am still learning"

while (True):
    user =input("You:")
    response =chatBot(user)
    print("Bot:",response)

    if "bye" in user.lower():
        break