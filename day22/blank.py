from turtle import Turtle

class Blank(Turtle):
    def __init__(self):
        super().__init__()
        self.blanks = []
        self.create_blank()
    def create_blank(self):
        for i in range(-280,281,20):
            blank1=Turtle()
            blank1.speed("fastest")
            blank1.pendown()
            blank1.shape("square")
            blank1.color("white")
            blank1.shapesize(0.5,0.1)
            blank1.penup()
            blank1.goto(x=0,y=i)
            self.blanks.append(blank1)
            
        
    