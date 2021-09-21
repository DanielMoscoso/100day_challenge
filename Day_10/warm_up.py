# Name formater:
def format_name(f_name, l_name):
    # first_name = f_name.lower().capitalize()  # One way of doing it.
    # last_name = l_name.lower().capitalize()
    first_name = f_name.title()  # Another way of doing it.
    last_name = l_name.title()

    return f"{first_name} {last_name}"


full_name = format_name("hOl", "HAL")
print(full_name)
