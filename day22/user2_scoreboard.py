from turtle import Turtle,Screen


class User2ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.score=0
        self.color("red")
        self.penup()
        self.goto(-25,270)
        self.hideturtle()
        self.write(f" {self.score}", True, align="center",font=("Arial",20,"normal"))
        
    def new_score(self):
        self.score+=1
        self.clear()
        self.penup()
        self.goto(-25,270)
        self.hideturtle()
        self.write(f"{self.score}", True, align="center",font=("Arial",20,"normal"))
        
    def win(self):
        self.penup()
        self.goto(0,0)
        self.write("USER 2 WIN", True, align="center",font=("Arial",30,"normal"))
        self.hideturtle()    