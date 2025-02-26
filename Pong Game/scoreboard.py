import turtle


class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.score_update()

    def score_update(self):
        self.clear()
        self.goto(-100, 170)
        self.write(self.l_score, align='center', font=('Comic Sans MS', 100, 'normal'))
        self.goto(
            100, 170)
        self.write(self.r_score, align='center', font=('Comic Sans MS', 100, 'normal'))

    def left_score(self):
        self.l_score += 1
        self.score_update()

    def right_score(self):
        self.r_score += 1
        self.score_update()
