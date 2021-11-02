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
    file.close()
