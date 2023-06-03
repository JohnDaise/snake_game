from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.high_score = self.read_high_score()
        self.update_scoreboard()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            new_high_score = str(self.score)
            self.write_high_score(new_high_score)
        self.score = 0
        self.update_scoreboard()

    @staticmethod
    def read_high_score():
        with open("data.txt") as file:
            contents = file.read()
            print(contents)
            return int(contents)

    @staticmethod
    def write_high_score(score):
        new_high_score = score
        with open("data.txt", mode="w") as file:
            file.write(new_high_score)
