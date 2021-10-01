from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# # ---------------------------- In case you need it ----------------------------
# import os
# os.getcwd()
# os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_17\\quiz_game')
# # ---------------------------- In case you need it ----------------------------

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
quiz.next_question()
