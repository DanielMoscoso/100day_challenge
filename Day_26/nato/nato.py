import pandas as pd
import os

# TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# os.chdir("./Day_26/nato")

nato_alphabet = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

answer = input("Enter a word or a setence: ")

answer.split()

nato_answer = {row.letter:}
