from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.penup()
        self.goto(0,random.randint(-250,250))
        self.setheading(random.randint(0,360))
        random_list=[10, -10]
        self.x_move= random.choice(random_list)
        self.y_move =random.choice(random_list)
    def move(self):
        current_x = self.xcor()
        current_y = self.ycor()
        next_x = current_x + self.x_move
        next_y = current_y + self.y_move
        self.goto(next_x,next_y)
    
    def hit_up(self):
        self.y_move = -1*self.y_move
    
    def hit_player(self):
        self.x_move = -1*self.x_move
        
