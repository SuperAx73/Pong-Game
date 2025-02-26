import turtle


import Cpu_paddler
from turtle import Screen
from ball import Ball
import time
import net
from scoreboard import Scoreboard

print('''
▗▗ ▗▖▗▄▄▄▖▗▖    ▗▄▄▖ ▗▄▖ ▗▖  ▗▖▗▄▄▄▖    
▐▌ ▐▌▐▌   ▐▌   ▐▌   ▐▌ ▐▌▐▛▚▞▜▌▐▌       
▐▌ ▐▌▐▛▀▀▘▐▌   ▐▌   ▐▌ ▐▌▐▌  ▐▌▐▛▀▀▘    
▐▙█▟▌▐▙▄▄▖▐▙▄▄▖▝▚▄▄▖▝▚▄▞▘▐▌  ▐▌▐▙▄▄▖    
            ▗▄▄▄▖▗▄▖                    
              █ ▐▌ ▐▌                   
              █ ▐▌ ▐▌                   
              █ ▝▚▄▞▘                   
        ▗▄▄▖  ▗▄▖ ▗▖  ▗▖ ▗▄▄▖           
        ▐▌ ▐▌▐▌ ▐▌▐▛▚▖▐▌▐▌              
        ▐▛▀▘ ▐▌ ▐▌▐▌ ▝▜▌▐▌▝▜▌           
        ▐▌   ▝▚▄▞▘▐▌  ▐▌▝▚▄▞▘           
                                                      
''')

play = input('''
▗▄▄▖ ▗▄▄▖ ▗▄▄▄▖ ▗▄▄▖ ▗▄▄▖     ▗▄▄▖▗▄▄▖  ▗▄▖  ▗▄▄▖▗▄▄▄▖    ▗▄▄▄▖▗▄▖      ▗▄▄▖▗▄▄▄▖▗▄▖ ▗▄▄▖▗▄▄▄▖
▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌   ▐▌       ▐▌   ▐▌ ▐▌▐▌ ▐▌▐▌   ▐▌         █ ▐▌ ▐▌    ▐▌     █ ▐▌ ▐▌▐▌ ▐▌ █  
▐▛▀▘ ▐▛▀▚▖▐▛▀▀▘ ▝▀▚▖ ▝▀▚▖     ▝▀▚▖▐▛▀▘ ▐▛▀▜▌▐▌   ▐▛▀▀▘      █ ▐▌ ▐▌     ▝▀▚▖  █ ▐▛▀▜▌▐▛▀▚▖ █  
▐▌   ▐▌ ▐▌▐▙▄▄▖▗▄▄▞▘▗▄▄▞▘    ▗▄▄▞▘▐▌   ▐▌ ▐▌▝▚▄▄▖▐▙▄▄▖      █ ▝▚▄▞▘    ▗▄▄▞▘  █ ▐▌ ▐▌▐▌ ▐▌ █  
                 ▗▄▖ ▗▄▄▖     ▗▄▄▄▖     ▗▄▄▄▖▗▄▖     ▗▄▄▄▖ ▗▖ ▗▖▗▄▄▄▖▗▄▄▄▖                    
                ▐▌ ▐▌▐▌ ▐▌    ▐▌ ▐▌       █ ▐▌ ▐▌    ▐▌ ▐▌ ▐▌ ▐▌  █    █                      
                ▐▌ ▐▌▐▛▀▚▖    ▐▌ ▐▌       █ ▐▌ ▐▌    ▐▌ ▐▌ ▐▌ ▐▌  █    █                      
                ▝▚▄▞▘▐▌ ▐▌    ▐▙▄▟▙▖      █ ▝▚▄▞▘    ▐▙▄▟▙▖▝▚▄▞▘▗▄█▄▖  █                      
                                                                                              
                                                                                              
''')
if play == ' ':
    players_points = 0
    cpu_points = 0
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("PONG")
    screen.tracer(0)


    class Menu(turtle.Turtle):

        def __init__(self):
            super().__init__()
            self.color('white')
            self.penup()
            self.hideturtle()
            self.show()

        def show(self):
            self.goto(0, 0)
            self.write('Welcome to PONG\nPress space to start\nor\n"q" to quit', align='center',
                       font=('Comic Sans MS', 50, 'normal'))


    Cpu_paddler.paddle2()
    Cpu_paddler.paddle1()
    ball = Ball()
    net.nett1(250)
    net.nett2(150)
    net.nett3(50)
    net.nett4(-50)
    net.nett5(-150)
    net.nett6(-250)
    net.nett7(-350)

    screen.listen()
    screen.onkey(Cpu_paddler.go_up_player, "Up")
    screen.onkey(Cpu_paddler.go_down_player, "Down")
    screen.onkey(Cpu_paddler.go_up_cpu, "w")
    screen.onkey(Cpu_paddler.go_down_cpu, "s")
    scoreboard = Scoreboard()

    on = True
    while on:
        screen.update()
        ball.move()
        time.sleep(0.05)

        if ball.ycor() > 280 or ball.ycor() < -270:
            ball.bounce()

        if ball.distance(Cpu_paddler.paddle) < 45 and ball.xcor() > 320:
            print('make contact')
            ball.hit()

        if ball.distance(Cpu_paddler.cpu_paddle) < 45 and ball.xcor() < -320:
            print('make contact')
            ball.hit()

         if ball.xcor() > 390:
            print('cpu point')
            cpu_points += 1
            scoreboard.left_score()
            ball.restart()
            ball.move()

        if ball.xcor() < -390:
            print('player point')
            players_points += 1
            scoreboard.right_score()
            ball.restart()
            ball.move()
    screen.exitonclick()
elif play == 'q':
    exit