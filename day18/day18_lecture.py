from turtle import Turtle,Screen
import random
tim =Turtle()

angel = [0,90,180,270]

tim.shape("turtle")
#x=4
# x=4 
# while x>0:
#   tim.fd(50)
#   tim.right(90)
#   x-=1
# while x>0:
#     y=6
#     while y>0:
#         tim.fd(40)
#         tim.penup()
#         tim.fd(40)
#         tim.pendown()
#         y-=1
    
#     tim.right(90)
#     x-=1

# for i in range(3,20):
#     x=i
#     angel=360/i
#     while i>0:
#         tim.fd(50)
#         tim.right(angel)
#         i-=1


# for _ in range(0,20):
#     tim.pensize(15)
#     tim.color(random.choices(colours))
#     tim.fd(50)
#     tim.heading(random.choices(angel))

def random_colours():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    random_colour=(r/255,g/255,b/255)
    return random_colour
color = random_colours()
# for _ in range(0,150):
#     random_colour=random_colours()
#     tim.pensize(15)
#     tim.color(random_colour)
#     tim.fd(50)
#     tim.right(random.choice(angel))    
# for i in range(0,360):
#     random_colour=random_colours()
#     tim.speed("fastest")
#     tim.pensize(1)
#     tim.color(random_colour)
#     tim.circle(100)
#     tim.setheading(i)    

for i in range(0,360,5):
    color = random_colours()
    
    tim.speed("fastest")
    tim.color(color)
    tim.circle(100)
    tim.setheading(i)

screen =Screen()
screen.exitonclick()