import time
from scoreboard import ScoreBoard
from turtle import Turtle,Screen
from food import Food
from snake import Snake
snake=Snake()
food=Food()
score=ScoreBoard()

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My snake game")

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
move=True

while(move):
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.segments[0].distance(food)<15:
        food.refresh()
        score.increase()
        snake.extend()
    # detect collsion with wall
    if (snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280):
        score.reset()
        snake.reset()
    # DETECT COLLSION WITH TAIL
    # IF HEAD COLLIDES WITH ANY SEGMENT WITH TAIL
    # TRIGGER GAME OVER
    for s_segments in snake.segments:
        if s_segments==snake.segments[0]:
            pass
        elif snake.segments[0].distance(s_segments)<9:
            score.reset()
            snake.reset()












screen.exitonclick()


