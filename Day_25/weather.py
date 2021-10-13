# import os
# os.getcwd()
# os.chdir("./Day_25/warm_up")
# # ------------------- Old way -------------------
# import csv
#
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# temperatures
# # ------------------- Old way -------------------

import pandas as pd

data = pd.read_csv("weather_data.csv")
data
print(data)
print(data["temp"])

# This is how you would create a dictionary out of a dataset.
data_dict = data.to_dict()
print(data_dict)

# This would turn a "series" into a "list".
print(data["temp"])
temp_list = data["temp"].to_list()

# You can take the average of a list:
avg = sum(temp_list) / len(temp_list)
avg

# Same in pandas:
data["temp"].mean()

# Geting the maximum number in a pandas series:
data["temp"].max()

# You can also get hold of the columns this way:
print(data["temp"])  # This is like a dictionary.
print(data.temp)  # This is like an object.

# Get data in rows:
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Access a specific location/index:
celcius = data[data.temp == data.temp.max()]
farenheit = (int(celcius.temp) * 9/5) + 32
print(farenheit)

# How to create a dataframe from scratch:
data_dict = {"students": ["Luis", "John", "Pedro"], "scores": [80, 70, 90]}

data = pd.DataFrame(data_dict)

# Then you can save that dataframe as a csv:
data.to_csv("new_data.csv")
