role = input("Enter your role ").strip().upper()
task = input("Enter your task ").strip()
tone = input("Enter tone: ").strip().capitalize()
prompt = f"Act as {role}. todays task is to create new {task}.keep it{tone}"
print("\n Generative Ai promt")
print(prompt)

