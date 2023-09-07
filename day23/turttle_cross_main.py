from turtle import Turtle,Screen
from player import Player
from car import Car
import time
myscreen = Screen()
myscreen.setup(800,600)
myscreen.bgcolor("white")
myscreen.tracer(0)
player= Player()

car=Car()
game_on = True
myscreen.listen()
myscreen.onkey(key="Up", fun=player.user_up)
myscreen.onkey(key="Down", fun=player.user_down)
myscreen.onkey(key="Right", fun=player.user_right)
myscreen.onkey(key="Left", fun=player.user_left)

for i in range(10):
    car.create_random_car()
    
while game_on:
    myscreen.update()
    car.create_car()
    car.car_move()
    if player.ycor() >280:
        car.new_level()
        player.penup
        player.goto(0,-280)
        player.setheading(90)    
    time.sleep(car.game_level)
    for cars in car.cars_list:
        
        if player.distance(cars)<14:
            car.hit_car()
            game_on=False
    
myscreen.exitonclick()