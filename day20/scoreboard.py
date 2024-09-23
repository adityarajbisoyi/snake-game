from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.score = 0
        with open("data.txt") as f:
            self.high_score = int(f.read())

        self.color("White")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} \tHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"Game Over !!", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as f:
                f.write(str(self.score))
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
