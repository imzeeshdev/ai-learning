person = {
    "name": "Xi",
    "skills": ["Python", "SQL"],
    "hours_per_week": 5,
    "city": "Malmö"
}

print(person["name"])
print(person["skills"][0])   # first item in the list
print(person["city"])

if person["hours_per_week"] >= 20:
    print("Full-time pace")
else:
    print("Part-time pace")

person["skills"].append("APIs")   # add to the list
print(person)

for skill in person["skills"]:
    print(skill)