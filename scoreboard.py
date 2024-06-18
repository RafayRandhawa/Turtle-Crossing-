from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(-270, 260)
        self.ht()
        self.color('black')
        self.pendown()

    def score_write(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=("Ariel", 24, "bold"))

    def current_level(self):
        return self.level
