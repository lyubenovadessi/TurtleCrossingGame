from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-210, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"🏁Level: {self.level} 🏆", align=ALIGNMENT, font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("💥GAME OVER💥", align=ALIGNMENT, font=FONT)



