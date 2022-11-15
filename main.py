from data import question_data
from question_model import Question
from quizbrain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    if quiz.next_question():
        quiz.print_score()
quiz.print_final_score()
