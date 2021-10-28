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
        self.make = kwargs["make"]
        self.model = kwargs["model"]


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.make)
