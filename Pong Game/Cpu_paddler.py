import turtle

paddle = turtle.Turtle()
cpu_paddle = turtle.Turtle()


def paddle2():
    cpu_paddle.shapesize(stretch_wid=5, stretch_len=0.5)
    cpu_paddle.color('white')
    cpu_paddle.shape("square")
    cpu_paddle.penup()
    cpu_paddle.setposition(-350, 0)


def paddle1():
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=0.5)
    paddle.penup()
    paddle.goto(350, 0)


def go_up_player():
    new_y = paddle.ycor() + 40
    paddle.goto(paddle.xcor(), new_y)


def go_down_player():
    new_y = paddle.ycor() - 40
    paddle.goto(paddle.xcor(), new_y)


def go_up_cpu():
    new_y_cpu = cpu_paddle.ycor() + 40
    cpu_paddle.goto(cpu_paddle.xcor(), new_y_cpu)


def go_down_cpu():
    new_y_cpu = (cpu_paddle.ycor() - 40)
    cpu_paddle.goto(cpu_paddle.xcor(), new_y_cpu)
