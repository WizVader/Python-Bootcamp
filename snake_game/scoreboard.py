from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.file = "data.txt"
        self.highscore = self.read_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def read_highscore(self):
        with open(self.file, "r") as file:
            return int(file.read())

    def write_highscore(self):
        with open(self.file, "w") as file:
            file.write(f"{self.score}")
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=('Courier', 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align = "center", font =('Courier', 20, "normal"))
