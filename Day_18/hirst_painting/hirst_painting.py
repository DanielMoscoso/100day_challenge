import colorgram


# ---------------------------- In case you need it ----------------------------
def reset_kernel():
    import os
    # os.getcwd()
    os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_18\\hirst_painting')
# ---------------------------- In case you need it ----------------------------


colors = colorgram.extract('spot_paint.gif', 40)

list_of_colors = []
for color in colors:
    list_of_colors.append(tuple(color.rgb))

print(list_of_colors)
