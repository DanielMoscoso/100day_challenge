# NOTE: 1
# # FileNotFoundError: [Errno 2] No such file or directory: 'a_file.txt'
# with open("a_file.txt") as file:
#     file.read()


# NOTE: 2
# # KeyError: 'hello'
# a_dictionary = {"key": "value"}
# value = a_dictionary["hello"]


# NOTE: 3
# # IndexError: list index out of range
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]


# NOTE: 4
# # TypeError: can only concatenate str (not "int") to str
# text = "abc"
# print(text + 9)
# %%
# NOTE: 1 + 2
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    value = a_dictionary["hello"]
except FileNotFoundError:  # You can leave it without the actual exception, just plain 'except' and it will still work.
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist!")
else:  # In case all the 'try' succeed.
    content = file.read()
    print(content)
finally:  # This will excecute no matter what.
    file.close()
    print("File was closed.")
# %%
# How to raise your own errors:
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height**2
print(bmi)

# %%
fruits = ["Apple", "Pear", "Orange"]


# Excersise 1:
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


# TODO: Catch the exception and make sure the code runs without crashing.
make_pie(4)
# %%
# Excersise 2:
facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        total_likes = total_likes + 0

print(total_likes)
# %%
# %%
# Excersise 3:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)

while True:
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
    else:
        print(output_list)
        break

# %%
# Or you can use recursion:
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
# %%
# %%
