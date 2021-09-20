programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary["Loop"])

print(programming_dictionary["Bug"])
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary["Bug"])

# How to loop through a dictionary:
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# ----------------------- This is dictionary unpacking: -----------------------
grades0 = {'John': 95, 'Jennifer': 98}
grades1 = {**grades0}
print(grades0)
print()
print(grades1)

# dictionary unpacking is different than dictionary aliasing:
# Aliasing
grades2 = grades0

grades1 is grades0  # This is dictionary unpacking.Therefore making a BRAND NEW OBJECT that has the same characteristics. That is why it is FALSE.
grades2 is grades0  # This is 'Aliasing'. It simply creates a reference to the same object.That is why it is TRUE.
# ----------------------- This is dictionary unpacking: -----------------------
# %%
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# --------------------- One way: ---------------------
student_grades = {}
for key in student_scores:
    if student_scores[key] > 90:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 80:
        student_grades[key] = "Exceeds Expectations"
    elif student_scores[key] > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
print()
# --------------------- One way: ---------------------

# ------------------- Another way: -------------------
student_grades = {}
for key, value in student_scores.items():
    if value > 90:
        student_grades[key] = "Outstanding"
    elif value > 80:
        student_grades[key] = "Exceeds Expectations"
    elif value > 70:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
# ------------------- Another way: -------------------
# %%
# Nesting lists and dictionaries:
# Lists inside dictionaries, inside dictionaries.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"],
               "total_visits": 10},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]}
}

# Dictionary inside a list:
[{1: [1, 3, 2], "hola": {}}, {1: "one", 2: "two"}]

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 10
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
]
# %%
travel_log = [
    {
        "country": "France",
        "total_visits": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "total_visits": 5,
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    }
]


def add_new_country(new_country="", visits=0, cities=[]):
    # new_dictionary = {"country": new_country, "total_visits": visits, "cities_visited": cities}  # This also works.
    new_dictionary = {}
    new_dictionary["country"] = new_country
    new_dictionary["total_visits"] = visits
    new_dictionary["cities_visited"] = cities
    travel_log.append(new_dictionary)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
# This is very interesting: It shows the different types of variables within the dictionat.
# print(travel_log[2])
# type(travel_log[2])
# type(travel_log[2]["cities_visited"])
# type(travel_log[2]["cities_visited"][0])
