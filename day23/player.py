from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_turtle()
        
    def create_turtle(self):
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        
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
        
    def user_right(self):
        current_y = self.ycor()
        current_x = self.xcor()
        new_x = current_x + 20
        self.goto(new_x,current_y)

    def user_left(self):
        current_y = self.ycor()
        current_x = self.xcor()
        new_x = current_x - 20
        self.goto(new_x,current_y)
