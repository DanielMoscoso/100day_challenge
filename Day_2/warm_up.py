# 2 digit addition
two_digit = input("Give me a 2 digit number and I will return the addition of them: ")

firt_digit = int(two_digit[0])
second_digit = int(two_digit[1])

addition = firt_digit + second_digit

print(addition)

# %%
# BMI Calculator:
height = float(input("What is your height? "))
weight = float(input("What is your weight?"))

BMI = weight / height**2

print(f"Your BMI is: {int(BMI)}")

# %%
# Life in days, weeks and months. (This is the simplest version: when you JUST turned that age, not even one day after).
print("Hello, I will calculate how many days, weeks and months you would have left until you turn 90-years-old.\n")

age = int(input("How old are you? You can type just the number: "))

years_remaining = 90 - age

days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, or {weeks_remaining} weeks, or {months_remaining} months before you turn 90-years-old.")
