from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank  = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_que = Question(question_text, question_answer)
    question_bank.append(new_que)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
else:
    print(f'''You've completed the quiz
Your final score was {quiz.score}/12''')
print("\nThank you for playing!")