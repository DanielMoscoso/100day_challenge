# Even or Odd:
answer = int(input("Type a number and I will tell you if it is even or odd: "))

if answer % 2:
    print("This is an odd number.")  # This is a little counter intuitive at first. But if you get an asnwer of 1, then remember that booleans are binary; 1=True and 0=False.
else:
    print("This is an even number.")
# %%
# OR:
answer = int(input("Type a number and I will tell you if it is even or odd: "))

if answer % 2 == 0:
    print("This is an even number.")  # This is a little counter intuitive at first. But if you get an asnwer of 1, then remember that booleans are binary; 1=True and 0=False.
else:
    print("This is an odd number.")
# %%
# %%
# BMI Calculator 2.0:
weight = float(input("What is your weight in Kilograms?: "))
height = float(input("What is your height in Meters?: "))

bmi = round(weight / height**2)

# Great for practice and understanding "if" and "comparisons":
if bmi < 18.5:
    print(f"Your BMI is: {bmi}, are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is: {bmi}, are normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is: {bmi}, are overweight.")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is: {bmi}, are obese.")
else:
    print(f"Your BMI is: {bmi}, are clinically obese.")

# %%
# But this is a better written code:
weight = float(input("What is your weight in Kilograms?: "))
height = float(input("What is your height in Meters?: "))

bmi = round(weight / height**2)

if bmi < 18.5:
    print(f"Your BMI is: {bmi}, are underweight.")
elif bmi < 25:  # If you check for it to be strictly below 18.5, then you know that when it enters this line, it is 18.5+. No need to check it again.
    print(f"Your BMI is: {bmi}, are normal weight.")
elif bmi < 30:
    print(f"Your BMI is: {bmi}, are overweight.")
elif bmi < 35:
    print(f"Your BMI is: {bmi}, are obese.")
else:
    print(f"Your BMI is: {bmi}, are clinically obese.")
# %%
# %%
# Leap year Calculator:
year = int(input("Which year do you want to check?: "))

if year % 4 == 0 and year % 100 != 0:
    print("It is a leap year!")
else:
    if year % 400 == 0:
        print("It is a leap year!")
    else:
        print("It is not a leap year.")
# %%
# Alternative way of solving the problem: This one supposedly is more readable. (But I disagree).
year = int(input("Which year do you want to check?: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("It is a leap year!")
        else:
            print("It is not a leap year.")
    else:
        print("It is a leap year!")
else:
    print("It is not a leap year.")
# %%
# %%
# Rollercoaster ride:
# This excercise is really good because it forces you to do things the simplest and most efficient way.
print("Welcome to the rollercoaster!")
bill = 0

height = int(input("What is your height in cm?: "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?: "))

    if age < 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    photo = input("Do you want a photo taken? (Y)es or (N)o?")
    if photo == "Y":
        bill += 3

    print(f"Your bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
# %%
