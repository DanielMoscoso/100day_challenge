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
