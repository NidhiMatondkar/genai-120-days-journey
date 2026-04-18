skills = ["Python", "AI", "ML"]

# add
skills.append("GenAI")

# remove
skills.remove("AI")

# loop
for skill in skills:
    print(skill)

# unpack
a, *others = skills
print(a)
print(others)