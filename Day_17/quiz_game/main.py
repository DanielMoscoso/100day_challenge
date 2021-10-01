from question_model import Question
from data import question_data
# # ---------------------------- In case you need it ----------------------------
# import os
# os.getcwd()
# os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_17\\quiz_game')
# # ---------------------------- In case you need it ----------------------------

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))
