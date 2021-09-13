# Even or Odd:
answer = int(input("Type a number and I will tell you if it is even or odd: "))

if answer % 2:
    print("This is an odd number.")  # This is a little counter intuitive at first. But if you get an asnwer of 1, then remember that booleans are binary; 1=True and 0=False.
else:
    print("This is an even number.")
