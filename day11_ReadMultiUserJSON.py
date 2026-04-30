import json

with open("MultiUser.json","r") as file:
    data = json.load(file)
    
    for person in data:
       print(f"Name: {person["name"]} | Age: {person["age"] } | Goal: {person["goal"]} ")

