from turtle import Turtle,Screen
import random
myscreen = Screen()
myscreen.setup(width=800,height=600)
bet =myscreen.textinput(title="Your bet",prompt="Which color will win")
colors = ["purple","red","orange","yellow","green","black","blue"]
y_coord = [150,100,50,0,-50,-100,-150]
racers =[]

for i in range(0,len(colors)):
    sam1 =Turtle(shape="turtle")
    sam1.color(colors[i])
    sam1.penup()
    sam1.goto(x=-380,y=y_coord[i])
    racers.append(sam1)
    
x=0
while x<1:
    for racer in racers:
        racer.forward(random.randint(0,25))
        
        if racer.xcor()>=400:
            racer.setheading(180)
            
        if racer.xcor() <= -400:
            race_color= racer.fillcolor()
            
            if bet == race_color:
                print(f"You win. {race_color} won")
                
            else:
                print(f"You lost. {race_color} won")
            
            x=1
        
    
myscreen.exitonclick()