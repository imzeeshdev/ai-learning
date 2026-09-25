name = "Xi"
city = "Malmö"
years_experience = 15

print("Name:", name)
print("City:", city)
print("Experience:", years_experience, "years")
print("Next year:", years_experience + 1, "years")

def greet(person):
    return "Hello, " + person + "!"

print(greet(name))
print(greet("world"))

skills = ["Python", "SQL", "APIs", "RAG"]
persons = ["Xi", "Asif", "Sara"]

for skill in skills:
    for person in persons:
        print(person, " is learning:", skill)

print("Total skills:", len(skills))

