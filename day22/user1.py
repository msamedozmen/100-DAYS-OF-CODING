from turtle import Turtle,Screen

class User1(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        
    def create_user(self):
        self.shape("square")
        self.color("white") 
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(x=350,y=0)    
        
    def user_up(self):
        current_y = self.ycor()
        current_x = self.xcor()
        new_y = current_y + 20
        self.goto(current_x,new_y)

    def user_down(self):
        current_y = self.ycor()
        current_x = self.xcor()
        new_y = current_y - 20
        self.goto(current_x,new_y)