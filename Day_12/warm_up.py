# -------------------- Scope --------------------
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
# %%
# This is a Block Scope in Java and C++  but not in Python:
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)  # This will not run on Java or C++ because the "Block Scope"
# %%
# Modifiying Global variables: Try not to use it, because can bring confusion down the road.
#                              Days and lines after writing the first variable.
enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# %%
# Instead do this:
enemies = 1


def increase_enemies():
    return enemies + 1


enemies = increase_enemies()
print(f"enemies inside function: {enemies}")
print(f"enemies outside function: {enemies}")
# %%
# Naming convention for global variables:
#   -Never modify them.
#   -All uppercased and separated with underscores.
PI = 3.14159


def calc():
    new = PI + 2
    return new


calc()
