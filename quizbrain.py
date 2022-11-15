import data


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ").capitalize()
            if user_answer == "True" or user_answer == "False":
                break
        return self.check_answer(current_question, user_answer)

    def check_answer(self, current_question, user_answer):
        if user_answer == current_question.answer:
            print("\tCorrect.")
            self.score += 1
            return True
        else:
            print("\tIncorrect.")
            return False

    def print_score(self):
        print(f"\tYour current score is: {self.score}/{self.question_number}.")

    def print_final_score(self):
        print(f"The End. You answered {self.score}/{self.question_number} questions correctly.")

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
