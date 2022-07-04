"""
Lession URL:
https://seir-222-sasquatch.netlify.app/second-language/week-18/day-3/labs/python-containers-lab/
"""
# Exercise 1
students = ["Joshua","Timmy","Json","Rusty","Javario", "Pi Hon"]
print(students[1])
print(students[-1])

#Exercise 2
foods = ("pizza", "pie", "Mac & Cheese", "Salsa", "Kimchi", "Louisiana fired chicken")
for food in foods:
    print(f'{food} is a good food')

# Exercise 3
for food in foods:
    if food == "Kimchi" or food == "Louisiana fired chicken":
        print(food)

#Exercise 4
home_town = {
    "city": "Long Beach",
    "state": "California",
    "population": "Lots"
}
print(f'I was born in {home_town["city"]}, {home_town["state"]} with a population of {home_town["population"]} ')

# Exercise 5
for prop in home_town:
    print(prop, home_town[prop])

# Exercise 6

cohort = []
for student in students:
    cohort.append(dict(
        name = zip(students),
        fav_food = zip(foods)
        ))
print(cohort)
food_test = zip(foods)

awesome_students = []

for student in students:
    awesome_students.append(f'{student} is awesome!')

for string in awesome_students:
    print (string)


