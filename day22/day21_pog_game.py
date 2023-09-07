from turtle import Turtle,Screen
from user1 import User1
from user2 import User2
from blank import Blank
from user1_scoreboard import User1ScoreBoard
from user2_scoreboard import User2ScoreBoard
import time
from ball import Ball
#Set up game screen
myscreen = Screen()
myscreen.setup(width=800,height=600)
myscreen.bgcolor("black")
myscreen.title("Pog Game")
myscreen.tracer(0.1)

#create user1
user1 = User1()
user1.create_user()
#create user2
user2 = User2()
user2.create_user()
ball = Ball()
#Set up screen to listen our command
myscreen.listen()
user1score=User1ScoreBoard()
user2score=User2ScoreBoard()
#User1 move
myscreen.onkey(key="Up", fun=user1.user_up)
myscreen.onkey(key="Down", fun=user1.user_down)

#User2 move
myscreen.onkey(key="W", fun= user2.upup)
myscreen.onkey(key="S", fun=user2.downdown)
myscreen.onkey(key="w", fun= user2.upup)
myscreen.onkey(key="s", fun=user2.downdown)
croos_line =Blank()
x=1


#create while loop for update steps
while x>0:
    myscreen.update()
    time.sleep(0.1)
    
    if x>0:
        ball.move()
        if ball.ycor()>270 or ball.ycor()<-270:
            ball.hit_up()
            
        if ball.distance(user1)<50 and ball.xcor() > 330 or ball.distance(user2)<50 and ball.xcor() < -330:
            ball.hit_player()
            if ball.x_move >= 10:
                ball.x_move +=1
            else:
                ball.x_move -=1
                
            if ball.y_move >= 10:
                ball.y_move +=1
            else:
                ball.y_move -=1
        if ball.xcor() > 350:
            user2score.new_score()
            ball.reset()
            ball=Ball()

        if ball.xcor()<-350:
            user1score.new_score()
            ball.reset()
            ball = Ball()

        if user1score.score == 10:
            user1score.win()
            x=1
        if user2score.score==10:
            user2score.win()
            x=-1

myscreen.exitonclick()