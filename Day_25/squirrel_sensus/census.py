import os
import pandas as pd

# os.getcwd()
# os.chdir("./Day_25/squirrel_census")

raw_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
raw_data
len(raw_data)

squirrels_dict = {}
for color in raw_data["Primary Fur Color"].unique():

    if type(color) == str:
        truth_table = raw_data["Primary Fur Color"] == color

        index = raw_data.index[truth_table]

        detailed_color_squirrels = raw_data.loc[index]  # All the info of the specific color.

        squirrels_dict[color] = len(detailed_color_squirrels)

squirrels_dict
data = pd.DataFrame(squirrels_dict, index=[0])
data
