# Ping Pong game

import turtle

window = turtle.Screen()
window.title("Ping Pong")
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.tracer(0)

#bar1
bar1 = turtle.Turtle()
bar1.speed(0)
bar1.shape("square")
bar1.color("blue")
bar1.penup() # make object dont print lines on screen
bar1.goto(-350,0)
bar1.shapesize(stretch_wid=5,stretch_len=1)

#bar2
bar2 = turtle.Turtle()
bar2.speed(0)
bar2.shape("square")
bar2.color("red")
bar2.penup()
bar2.goto(350,0)
bar2.shapesize(stretch_wid=5,stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .1
ball.dy = .1

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)

#functions
def bar1_up():
    y = bar1.ycor()
    y += 20
    bar1.sety(y)

def bar2_up():
    y = bar2.ycor()
    y += 20
    bar2.sety(y)

def bar1_down():
    y = bar1.ycor()
    y -= 20
    bar1.sety(y)

def bar2_down():
    y = bar2.ycor()
    y -= 20
    bar2.sety(y)

    

#keyboard bindings
window.listen()
window.onkeypress(bar1_up, "w")
window.onkeypress(bar2_up, "Up")
window.onkeypress(bar1_down, "s")
window.onkeypress(bar2_down, "Down")




while True:
    window.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 +=1
        score.clear()
        score.write(f"Blue : {score1} Red : {score2}", align="center", font=("Courier",24,"normal"))

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write(f"Blue : {score1} Red : {score2}", align="center", font=("Courier",24,"normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bar2.ycor() + 40 and ball.ycor() > bar2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() > bar1.ycor() - 40 and ball.ycor() < bar1.ycor() + 40):
        ball.setx(-340)
        ball.dx *= -1
        

    


