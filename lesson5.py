import json

person = {
    "name": "Xi",
    "city": "Malmö",
    "skills": ["Python", "SQL", "APIs"],
}

# Save the dictionary to a file
#with open("person.json", "w", encoding="utf-8") as f:
#    json.dump(person, f, indent=2, ensure_ascii=False)


def add_skill(filename, skill):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)

    if skill not in data["skills"]:
        data["skills"].append(skill)
    
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

add_skill("person.json", "Git")

# Read it back
with open("person.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["name"])
print(loaded["city"])
print(loaded["skills"])