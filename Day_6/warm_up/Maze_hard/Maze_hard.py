#  This is the corect way of doing it. It will always choose go right first if
#  it can!!! (It is facing forward to the left, after leaving the dead alley):
#                        \   \''''\
#                       __\   \    \
#                       ___<-X______\
def turn_right():
    turn_left()
    turn_left()
    turn_left()


right_token = 0
while not at_goal():
    # This is in case it gets stuck in an infinite loop going always right because it is allowed.
    if right_token > 3:
        turn_left()
        right_token = 0

    if right_is_clear():  # This is the correct way!
        turn_right()
        move()  # It turns right AND moves forward in order to get out of the possible infinite loop in the maze.
        right_token += 1
    elif front_is_clear():
        move()
    else:
        turn_left()
        right_token -= 1
# %%
# %%


# Cool clever, and different way of seeing the infinite loop problem inside the maze:
def turn_right():
    turn_left()
    turn_left()
    turn_left()


#  This will always make sure that the robot first hits a wall, turns to the left, and starts from there:
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():  # This is the correct way!
        turn_right()
        move()  # It turns right AND moves forward in order to get out of the possible infinite loop in the maze.
    elif front_is_clear():
        move()
    else:
        turn_left()

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
