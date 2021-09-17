#  This code is incorrect, because every time it sees it can go forward, it will.
#  What happens here? (It is facing forward to the left, after leaving the dead alley):
#                        \   \''''\
#                       __\   \    \
#                       ___<-X______\

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear():  # This is the culprit!
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
    else:
        pass

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
