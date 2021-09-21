# Name formater:
def format_name(f_name, l_name):
    """
    Take a first and last name and format it to return the title case version of the entire name.
    """
    if f_name == "" or l_name == "":
        return "You did not provide a valid input. Please try again."

    # first_name = f_name.lower().capitalize()  # One way of doing it.
    # last_name = l_name.lower().capitalize()
    first_name = f_name.title()  # Another way of doing it.
    last_name = l_name.title()

    return f"{first_name} {last_name}"


full_name = format_name("hOl", "HAL")
print(full_name)
help(format_name)

# %%

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year=0, month=0):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # This is for normal years.

    if month > 12 or month < 1:
        return "Invalid input."

    if year < 0:
        return"Invalid input."

    if is_leap(year) and month == 2:
        return f"It is a leap year, therefore, there are {month_days[month-1]+1} days in that month."
    elif is_leap(year):
        return f"It is a leap year, therefore, there are {month_days[month-1]} days in that month."
    else:
        return f"It is not a leap year, therefore, there are {month_days[month-1]} days in that month."


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
