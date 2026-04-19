user_input = input("You: ").strip().lower()

if "hello" in user_input:
    print("Bot: Hi there 👋")
elif "name" in user_input:
    print("Bot: My name is GenAI Bot 🤖")
elif "skill" in user_input:
    print("Bot: You are learning Python and AI 🚀")
elif "age" in user_input:
    print("Bot: I don't have age 😄")
elif "bye" in user_input:
    print("Bot: Goodbye! See you soon 👋")
else:
    print("Bot: I'm still learning, ask something else 😅")