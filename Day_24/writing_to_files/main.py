# import os
#
# os.getcwd()
# os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_24\\writing_to_files')

# Reading a file:
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Writing a file:
with open("my_new_file.txt", "a") as file:
    file.write("\nNew text.")
