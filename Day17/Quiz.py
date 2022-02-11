# The main file for Quiz from the Question_Model and data
from Quiz_brain import QuizBrain
from data import question_data
from Question_Model import Question

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz has been completed and You have scored {quiz.score} / {quiz.question_number}")