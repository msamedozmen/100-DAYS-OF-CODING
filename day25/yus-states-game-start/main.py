import turtle
import pandas as pd

myscreen = turtle.Screen()
myscreen.title("US States Game")
image = "yus-states-game-start\yblank_states_img.gif"
myscreen.addshape(image)

turtle.shape(image)

# def get_xy(x,y):
#     print(x,y)
    
# turtle.onscreenclick(get_xy)
data = pd.read_csv("us-states-game-start\50_states.csv")
count = 0

while count<50:
    user_answer = turtle.textinput(title=f"{count}/50 States Name", prompt="Type states name")

turtle.mainloop()