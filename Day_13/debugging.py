# ==================================== DONE ====================================
number = int(input("Which number do you want to check?"))

if number % 2 = 0:  # You should not assign the value "0", but compare it instead > "=="
    print("This is an even number.")
else:
    print("This is an odd number.")
# ==================================== DONE ====================================
# %%
# ==================================== DONE ====================================
year = input("Which year do you want to check?")  # You should be turning the answer into an "int". Right now it is a "str".

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
# ==================================== DONE ====================================
# %%
# 1.-The final print is printing a number inside a list.
# 2.-You should be using 'elif' to make one big condition, and not a bunch of small ones.
# 3.-You should use "and" instead of "or".
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])
