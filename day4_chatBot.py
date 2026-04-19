skills = []
for i in range(3):
    skill = input(f"Entere skill{i+1}").strip()
    skills.append(skill)
print("\n Your skills are")
for skill in skills:
    print(skill)
first , *others = skills
print("\nPrimary Skill is :",  first)
print("\n others skills are :",   others)