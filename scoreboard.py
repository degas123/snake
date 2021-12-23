from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 24, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        with open("data.txt")as file:
            self.high_score = int(file.read())

    def score(self):
        self.clear()
        self.color("green")
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.write(f"Score:  {self.game_score} High score : {self.high_score}", False, ALIGNMENT, FONT)

    def add_score(self):
        self.game_score += 1

    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
            with open("data.txt", mode="w")as file:
                file.write(str(self.high_score))
        self.game_score = 0

    # def border(self):
    #     self.color("red")
    #     self.fd(50)
