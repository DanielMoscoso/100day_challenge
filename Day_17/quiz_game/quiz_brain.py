from main import question_bank
# # ---------------------------- In case you need it ----------------------------
# import os
# os.getcwd()
# os.chdir('C:\\Users\\Daniel\\Documents\\Python\\100days\\Day_17\\quiz_game')
# # ---------------------------- In case you need it ----------------------------


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}: {current_question.text}  (True/False): ").lower()
