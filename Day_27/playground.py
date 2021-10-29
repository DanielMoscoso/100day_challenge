# *args:
def add(*args):
    token = 0
    for item in args:
        token += item

    return token


# or
def add2(*args):
    return sum(args)


add(1, 2, 3, 4)
add2(1, 2, 3, 5)


# %%
# **kwargs:
def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=5)


# %%
# classes and **kwargs:
class Car:
    def __init__(self, **kwargs):
        # Dictionaries also have a bilt in function called "get()":
        # It returns the value that is bein accessed if it exists. If it does not
        # then the code does not crash.
        self.make = kwargs.get("model")
        self.model = kwargs.get("make")
        self.model = kwargs.get("color")
        self.model = kwargs.get("seats")


my_car = Car(make="Nissan")
print(my_car.model)
print(my_car.make)  # This does not crash anymore.
