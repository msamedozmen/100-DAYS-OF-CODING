from turtle import Turtle,Screen

sam = Turtle()
myscreen = Screen()


def move_forwards():
    sam.forward(18)
def move_backwards():
    sam.backward(18)

def move_left():
    left = sam.heading() + 15
    sam.setheading(left)
def move_right():
    right = sam.heading() - 15
    sam.setheading(right)
def clear():
    sam.clear()
    sam.penup()
    sam.home()
    sam.pendown()
        
def pen_up():
    sam.penup()

def pen_down():
    sam.pendown()

def delete_last_move():
    sam.undo()
myscreen.listen()
myscreen.onkey(key="w", fun=move_forwards)
myscreen.onkey(key="s", fun=move_backwards)
myscreen.onkey(key="a", fun= move_left)
myscreen.onkey(key="d", fun=move_right)
myscreen.onkey(key="c", fun=clear)
myscreen.onkey(key="q", fun=pen_up)
myscreen.onkey(key="e", fun=pen_down)
myscreen.onkey(key="space", fun=delete_last_move)

myscreen.exitonclick()