from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
myscreen = Screen()
myscreen.setup(width=800, height=800)
myscreen.bgcolor("black")
myscreen.title("Snake Game")
myscreen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()
myscreen.listen()
myscreen.onkey(key="Up", fun=snake.up)
myscreen.onkey(key="Down", fun=snake.down)
myscreen.onkey(key="Left", fun= snake.left)
myscreen.onkey(key="Right", fun=snake.right)
# snakes_body =[]
# x_cor=[-20,0,20]
# for i in range(0,len(x_cor)):
    
#     snake_body = Turtle()
#     snake_body.shape("square")
#     snake_body.color("white")
#     snake_body.penup()
#     snake_body.goto(x=x_cor[i],y=0)
#     snakes_body.append(snake_body)

movement=1
score=0
while movement>0:
    
    myscreen.update()
    time.sleep(0.1)
    # score=0
    # new_x = snakes_body[-1].xcor()
    # new_y = snakes_body[-1].ycor()
    #snake.move()
    # for snake in range(0 ,len(snakes_body)-1,1):
    #     last_x= snakes_body[snake +1].xcor()
    #     last_y= snakes_body[snake +1].ycor()
    #     snakes_body[snake].goto(last_x,last_y)
    #new_score = score +1
    # if new_score > score:
    #         snake_body = Turtle()
    #         snake_body.shape("square")
    #         snake_body.color("white")
    #         snake_body.penup()
    #         snake_body.goto(new_x,new_y)
    #         snakes_body.append(snake_body)
    # score=1
    snake.move()
    if snake.snakes_body[0].distance(food)<15:
        score +=1
        food.new_location()
        snake.new_body()
        score_board.new_score()
    if snake.snakes_body[0].xcor()>380 or snake.snakes_body[0].xcor()<-380 or snake.snakes_body[0].ycor()>380 or snake.snakes_body[0].ycor()<-380:
        score_board.reset_game()
        snake.reset_snake()
        #score_board.game_over()
        #movement =0
    if snake.hit_tail() ==1:
        score_board.reset_game()
        snake.reset_snake()

        #score_board.game_over()
        #movement=0
    # snakes_body[-1].forward(20)
    # snakes_body[-1].left(90)

myscreen.exitonclick()