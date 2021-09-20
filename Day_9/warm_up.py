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
