#  This is the corect way of doing it. It will always choose go right first if
#  it can!!! (It is facing forward to the left, after leaving the dead alley):
#                        \   \''''\
#                       __\   \    \
#                       ___<-X______\
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if right_is_clear():  # This is the correct way!
        turn_right()
        move()  # It turns right AND moves forward in order to get out of the possible infinite loop in the maze.
    elif front_is_clear():
        move()
    elif not front_is_clear() and not right_is_clear():
        turn_left()
    else:
        pass

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
