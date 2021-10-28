def add(*args):
    token = 0
    for item in args:
        token += item

    return token


add(1, 2, 3, 4)
