# This code will calculate the average student height in a classroom.
# NOTE: there are functions like "len()", "enumerate()" or "sum()" that can make your life
#       way simpler if you use them inside the for loop. but the challenge here is to figure
#       out a way to use the for loop to do it.
student_heights = input("Input a list of student heights separated by a space.").split()  # 156 178 165 171 187
total_height = 0
iterations = 0

for n in range(0, len(student_heights)):  # Remember, range is exclusive, that is why you do not need the "-1"
    student_heights[n] = int(student_heights[n])
    total_height += student_heights[n]
    iterations += 1

average_height = total_height / iterations

print(f"The average height is : {round(average_height)}")
# %%
# It can also be done this way (which I preffer)
student_heights = input("Input a list of student heights separated by a space.").split()  # 156 178 165 171 187
total_height = 0
iterations = 0

for student in student_heights:  # 156 178 165 171 187
    total_height += int(student)
    iterations += 1

average_height = total_height / iterations

print(f"The average height is : {round(average_height)}")
# %%
# %%
# Now you are using the same code as before, but outputing the highest exam score from the list.
# NOTE: Again, you have the function "max()" that does this, but try to figure out a way around it.
student_scores = input("Input a list of student heights separated by a space.").split()
max_score = 0

for score in student_scores:  # 78 65 89 86 55 91 64 89
    student_score = int(score)

    if max_score < student_score:
        max_score = student_score

print(f"The highest score in the class is : {max_score}")
# %%
# %%
# Sum all the EVEN numbers in a range of numbers.
token = 0
for number in range(1, 101):
    if not number % 2:  # The "not" essentially makes the 0 from the remainder, and makes it 1, so it would be true for the statement.
  # if number % 2 == 0:  # The normal way.
        token += number
print(token)
# %%
# OR
token = 0
for number in range(2, 101, 2):
    token += number
print(token)
