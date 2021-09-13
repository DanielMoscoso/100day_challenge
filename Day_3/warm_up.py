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
    elif age >= 45 and age <= 55:
        print("Everythin is going to be ok. Have a free ride on us!")
        bill = 0
    else:
        bill = 12

    photo = input("Do you want a photo taken? (Y)es or (N)o?")
    if photo == "Y":
        bill += 3

    print(f"Your bill is ${bill}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
# %%
# %%
# Pizza order program:
print("Welcome to the Python Pizza Deliveries!")

size = input("What size do you want? (S)mall, (M)edium or (L)arge?:")
pepperoni = input("Do you want to add pepperoni? (Y)es or (N)o?: ")
extra_cheese = input("Do you want extra cheese? (Y)es or (N)o?: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if pepperoni == "Y" and size == "S":
    bill += 2
elif pepperoni == "Y" and size != "S":
    bill += 3
else:
    pass

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
# %%
# Nested if statements:
print("Welcome to the Python Pizza Deliveries!")

size = input("What size do you want? (S)mall, (M)edium or (L)arge?:")
pepperoni = input("Do you want to add pepperoni? (Y)es or (N)o?: ")
extra_cheese = input("Do you want extra cheese? (Y)es or (N)o?: ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    pass

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

# %%
# %%
# Love calculator:
print("Welcome to the love calculator!")

name1 = input("What is your name?: ")
name2 = input("What is their name?: ")

t = name1.lower().count("t") + name2.lower().count("t")
r = name1.lower().count("r") + name2.lower().count("r")
u = name1.lower().count("u") + name2.lower().count("u")
e = name1.lower().count("e") + name2.lower().count("e")
l = name1.lower().count("l") + name2.lower().count("l")
o = name1.lower().count("o") + name2.lower().count("o")
v = name1.lower().count("v") + name2.lower().count("v")

first_half = t + r + u + e
second_half = l + o + v + e

str_complete = str(first_half) + str(second_half)  # This adds the 2 numbers to make the %.
int_complete = int(str_complete)  # This will turn the final output into an integer.

if int_complete < 10 or int_complete > 90:
    print(f"Your score is {int_complete}%, you go together like coke and mentos.")
elif int_complete >= 40 and int_complete <= 50:
    print(f"Your score is {int_complete}%, you are alright together.")
else:
    print(f"Your score is {int_complete}%.")
