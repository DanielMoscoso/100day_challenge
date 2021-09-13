print("Welcome to the tip calculator.")

total = float(input("What is the total bill? $"))
tip = int(input("What percentage tip would you give? 10%, 12%, or 15%? ")[:2])  # [:2] will make sure that no other character will be taken in after the firt 2 digits.
people = int(input("How many people to split the bill? "))

final_amount = total + (total * tip / 100)
pay_per_person = final_amount / people

print(f"Each person should pay: ${round(pay_per_person, 2)}")
# print(f'Each person should pay: ${"{:.2f}".format(pay_per_person)}')  # This will output 2 decimal places, even if the last digit is 0.
