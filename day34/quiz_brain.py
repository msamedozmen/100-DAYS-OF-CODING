import html

# class QuizBrain:

#     def __init__(self, q_list):
#         self.question_number = 0
#         self.score = 0
#         self.question_list = q_list
#         self.current_question = None

#     def still_has_questions(self):
#         return self.question_number < len(self.question_list)

#     def next_question(self):
#         self.current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
#         self.check_answer(user_answer)

#     def check_answer(self, user_answer):
#         correct_answer = self.current_question.answer
#         if user_answer.lower() == correct_answer.lower():
#             self.score += 1
#             print("You got it right!")
#         else:
#             print("That's wrong.")

#         print(f"Your current score is: {self.score}/{self.question_number}")
#         print("\n")



class QuizBrain:
    def __init__(self,question_bank):
        self.question_number = 0
        self.question_list = question_bank
        self.score =0
        self.current_question = None
    def still_has_question(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            False
            
    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        text = html.unescape(self.current_question.text)
        self.question_number +=1
        # your_answer = input(f"Q.{self.question_number}: {text}").lower()
        real_answer = self.current_question.answer
        # self.checking_answer(your_answer)
        return (f"Q.{self.question_number}: {text}")
    def checking_answer(self,user_answer,real_answer):  
        self.user_answerr = user_answer
        self.reall_answer = real_answer
        if self.user_answerr == self.reall_answer.lower():
            self.score+=1     
            # print(f"You correct!! Your current Score is {self.score}/{self.question_number}")
            return 1
        # else:
            # print(f"You wrong. Correct answer : {self.reall_answer} Your current score{self.score}/{self.question_number}")

