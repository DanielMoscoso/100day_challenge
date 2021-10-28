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
