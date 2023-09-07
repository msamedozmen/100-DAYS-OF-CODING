import colorgram
from turtle import Turtle,Screen
import random
rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r =color.rgb.r
    g =color.rgb.g
    b =color.rgb.b
    new_color=(r/255,g/255,b/255)
    rgb_colors.append(new_color)

print(rgb_colors)

tim=Turtle()

x=6

tim.speed("fastest")
while x>0:
    tim.hideturtle()
    lef_circle_count= 12
    while lef_circle_count >0:
        tim.pendown()
        tim.dot(20,random.choice(rgb_colors))
        tim.penup()
        tim.fd(30)
        lef_circle_count-=1
        
    tim.dot(20,random.choice(rgb_colors))
    tim.penup
    tim.right(270)
    tim.fd(30)
    tim.right(270)
    tim.fd(360)
    tim.setheading(0)
    
    # while right_circle_count >0:
        
    #     tim.pendown()
    #     tim.dot(10,random.choice(rgb_colors))
    #     tim.penup()
    #     tim.fd(30)
        
    #     right_circle_count-=1
        
    # tim.dot(10,random.choice(rgb_colors))
    # tim.penup
    # tim.right(90)
    # tim.fd(10)
    # tim.right(90)    
    x-=1
screen =Screen()

screen.exitonclick()