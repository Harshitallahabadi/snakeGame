from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("High Score.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update()
    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}", align="center", font=("Aerial", 24, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.update()
    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("High Score.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score=0
        self.update()
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center",font="Aerial")
