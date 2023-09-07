# from question_model import Question
# from data import question_data
# from quiz_brain import QuizBrain

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")




from question_model import Question
from data import question_data,parameters
from quiz_brain import QuizBrain
from ui import QuizInterface


used_question = []
question_count = parameters["amount"]
print(question_count)
for i in range(0,question_count):
    new_question = Question(question_data[i]["question"],question_data[i]["correct_answer"])
    used_question.append(new_question)
print(len(used_question))
quiz=QuizBrain(used_question)
ui = QuizInterface(quiz)

while quiz.still_has_question():
    quiz.next_question()
