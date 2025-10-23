from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []

for q in question_data:
    q_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(q_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

