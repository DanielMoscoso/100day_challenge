import os

numbers = [1, 2, 3]
new_numbers = [item + 1 for item in numbers]

print(new_numbers)
# %%
name = "Daniel"
letters_list = [letter for letter in name]

print(letters_list)
# %%
numbers = [number * 2 for number in range(1, 5)]

print(numbers)
# %%
names = ["Jose", "Juan", "Pedro", "Maria", "Andres"]

short_names = [name for name in names if len(name) <= 4]

print(short_names)
# %%
names = ["Jose", "Juan", "Pedro", "Maria", "Andres"]

upper = [name.upper() for name in names if len(name) > 4]

print(upper)
# %%
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [number**2 for number in numbers]

print(squared_numbers)
# %%
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [number for number in numbers if number % 2 == 0]

print(result)
# %%
import pandas as pd

raw1 = pd.read_csv("file1.txt", header=None)
file1 = raw1[0].tolist()

raw2 = pd.read_csv("file2.txt", header=None)
file2 = raw2[0].tolist()

file1

result = [file1[number] for number in range(len(file1)) if file1[number] in file2]
# result = [number for number in file1 if number in file2]  # Same thing, but easier.

print(result)

# or

with open("file1.txt") as file1:
    data3 = file1.readlines()

with open("file2.txt") as file2:
    data4 = file2.readlines()

result = [int(number) for number in data3 if number in data4]

print(result)
# %%
import random

names = ["Jose", "Juan", "Pedro", "Maria", "Andres"]

# {ney_key: new_value for item in list}
student_scores = {student: random.randint(1, 100) for student in names}
student_scores

# {new_key: new_value for (key, value) in dictionary.items() if test}
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
passed_students
# %%
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word: len(word) for word in sentence.split()}

print(result)
# %%
# Celcius to Farenheit -> (temp_c * 9/5) + 32 = temp_f

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day: (temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
# %%
import pandas as pd

student_dict = {"student": ["Angela", "James", "Lily"],
                "score": [56, 76, 98]}

student_df = pd.DataFrame(student_dict)

student_df

# Loop through a Pandas data frame:
for (index, row) in student_df.iterrows():
    print(row)
    print()
    print(row.student)
    print()
    print(row.score)
    print()
    print()
# %%
