from turtle import Turtle
import random
import time
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.color_list=["purple","red","orange","yellow","green","black","blue"]
        self.game_level = 0.6
        self.penup()
        self.goto(-350,280)
        self.write(f"Current Level : {self.level} ", True, align="center",font=("Arial",10,"normal"))
        self.hideturtle()
        self.cars_list=[]
    
    def create_random_car(self):
        cars= Turtle()
        cars.showturtle()
        cars.shape("square")
        cars.shapesize(0.7,1.4)
        cars.color(random.choice(self.color_list))
        cars.penup()
        cars.goto(random.randint(-300,300),random.randint(-240,270))
        cars.setheading(180)   
        self.cars_list.append(cars)
  
    def create_car(self):
        cars= Turtle()
        cars.showturtle()
        cars.shape("square")
        cars.shapesize(0.7,1.4)
        cars.color(random.choice(self.color_list))
        cars.penup()
        cars.goto(350,random.randint(-240,270))
        cars.setheading(180)
        self.cars_list.append(cars)
            
    def car_move(self):
        for i in range(0, len(self.cars_list)):
            self.cars_list[i].forward(random.randint(0,20))
            
    def new_level(self):
        self.clear()
        self.level+=1
        self.game_level = (1/self.level)
        self.penup()
        self.goto(-350,280)
        self.write(f"Current Level : {self.level} ", True, align="center",font=("Arial",10,"normal"))
        self.create_car()
        
    def hit_car(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", True, align="center",font=("Arial",30,"normal"))
        self.hideturtle()