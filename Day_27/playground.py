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
