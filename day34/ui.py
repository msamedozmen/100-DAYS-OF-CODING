from tkinter import *
import tkinter as tk
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.my_screen = Tk()
        self.my_screen.config(padx=20,pady=20,bg=THEME_COLOR)
        self.my_screen.title("QuizLet")
        self.wrong_img = PhotoImage(file="images/false.png")
        self.true_img= PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_img,highlightthickness=0,command=self.true)
        self.true_button.grid(column=0,row=2,sticky=tk.S)
        self.wrong_button = Button(image=self.wrong_img,highlightthickness=0,command=self.false)
        self.wrong_button.grid(column=1,row=2,sticky=tk.S)        
        # self.blank_label = Label(bg=THEME_COLOR)
        # self.blank_label.grid(column=0,row=0)
        self.score_label = Label(bg=THEME_COLOR,text=f"Score: {self.score}",fg="white",font=("Arial",15,"bold"))
        self.score_label.grid(column=1,row=0)
        self.question_canvas = Canvas(width=300,height=250)
        self.current_question = self.question_canvas.create_text(150,125,fill="black",width = 280,font=("Arial",17,"italic"),text="benananansdanndasnda")
        self.question_canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.get_next_question()
        self.my_screen.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_question():
            self.question_canvas.config(bg="white")
            self.q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.current_question,text=self.q_text)
        else:
            self.question_canvas.itemconfig(self.current_question,text=f"You have reached end of your quiz.\n Your Score : {self.score}")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def true(self):
        user_answer = "true"
        if self.quiz.checking_answer(user_answer,self.quiz.current_question.answer) ==1:
            self.question_canvas.config(bg="green")
            self.score+=1
            self.score_label.config(text=f"Score:{self.score}")
        else:
            self.question_canvas.config(bg="red")

            self.score =self.score
        self.my_screen.after(300,func=self.get_next_question)               
    def false(self):
        user_answer = "false"
        if self.quiz.checking_answer(user_answer,self.quiz.current_question.answer) ==1:
            self.question_canvas.config(bg="green")
            self.score+=1
            self.score_label.config(text=f"Score:{self.score}")
        else:
            self.question_canvas.config(bg="red")
            
            self.score =self.score
        self.my_screen.after(300,func=self.get_next_question)       