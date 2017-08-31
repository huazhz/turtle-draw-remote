
# CCV Python Programming class activity: Modules and Functions
# Module 4
# RonP_Swing.py
# Ron Pulcer
# 11/15/2015

import turtle
import time

def hop(turt, radius, angle):
    turt.circle(radius, -angle * 2)

def pendulum_setup(turt, radius, angle):
    turt.circle(radius, -angle)

def pendulum(turt, radius, angle):
    turt.circle(radius, angle * 2)
    turt.circle(radius, -angle * 2)

def hopAlong(turt, direction="up", radius=25, angle=90, count=10, acceleration=0, startSpeed=5):
    # Direction can be: up, down, north, south, +, - (case insensitive)
    direction = direction.lower()
    if direction == "north" or direction == "+":
        direction = "up"
    elif direction == "south" or direction == "-":
        direction = "down"
    elif direction != "up" and direction != "down":
        # Set default value when input param not a valid choice
        direction = "up"

    turt.speed(startSpeed)
    sign = 1
    for n in range(count):
        if direction == "up":
            hop(turt, radius * sign, angle * sign)
        else:
            hop(turt, -radius * sign, angle * sign)

        if turt.speed() + acceleration < 1:
            turt.speed(1)
        elif turt.speed() + acceleration > 10:
            turt.speed(10)
        else:
            turt.speed(turt.speed() + acceleration)

        sign = sign * -1


def swingIt(turt, direction="up", radius=100, angle=90, count=10, acceleration=0, startSpeed=5):
    # Direction can be: up, down, north, south, +, - (case insensitive)
    direction = direction.lower()
    if direction == "north" or direction == "+":
        direction = "up"
    elif direction == "south" or direction == "-":
        direction = "down"
    elif direction != "up" and direction != "down":
        # Set default value when input param not a valid choice
        direction = "up"

    turt.penup()
    pendulum_setup(turt, radius, angle)
    turt.pendown()

    turt.speed(startSpeed)
    for n in range(count):
        if direction == "up":
            pendulum(turt, radius, angle)
        else:
            pendulum(turt, -radius, angle)

        if turt.speed() + acceleration < 1:
            turt.speed(1)
        elif turt.speed() + acceleration > 10:
            turt.speed(10)
        else:
            turt.speed(turt.speed() + acceleration)


if __name__ == "__main__":
    t = turtle.Turtle()
    scr = t.getscreen()

    # Unit Test cases when module is run standalone

    t.penup()
    t.goto(-250,-200)
    pendulum_setup(t, 100, 90)
    t.pendown()
    t.color("black")
    t.speed(1)
    pendulum(t, 100, 90)
    t.speed(3)
    pendulum(t, 100, 90)
    t.speed(5)
    pendulum(t, 100, 90)
    time.sleep(3)


    t.penup()
    t.goto(-50,150)
    t.pendown()
    t.color("red")
    hop(t, 100, 90)
    hop(t, -100, -90)

    t.pendown()
    t.color("orange")
    hop(t, -100, -90)
    hop(t, 100, 90)
    time.sleep(3)
    t.backward(20)

    t.pendown()
    t.color("gray")
    hop(t, 100, -90)
    hop(t, -100, 90)

    t.pendown()
    t.color("blue")
    hop(t, -100, 90)
    hop(t, 100, -90)
    time.sleep(3)


    t.penup()
    t.goto(-150,-100)
    t.pendown()
    t.color("green")
    hop(t, -200, 45)
    t.forward(20)

    t.pendown()
    t.color("orange")
    hop(t, -200, -45)
    t.backward(20)

    t.penup()
    t.goto(-275,150)
    t.pendown()
    t.color("darkgreen")
    hop(t, 100, 90)
    hop(t, -100, 90)
    t.forward(20)
    hop(t, -100, -90)
    hop(t, 100, -90)
    time.sleep(3)

    t.penup()
    t.goto(-250,0)
    t.pendown()
    t.color("red")
    hopAlong(t, "north")
    hopAlong(t, "south")
    time.sleep(3)

    t.penup()
    t.goto(200,-200)
    t.pendown()
    t.color("orange")
    t.setheading(0)
    hopAlong(t, "down", 60, 30, 3, 1, 5)
    t.color("blue")
    t.setheading(90)
    hopAlong(t, "up", 60, 45, 4, 1, 5)
    t.color("red")
    t.setheading(180)
    hopAlong(t, "+", 60, 54, 5, 1, 5)
    t.color("green")
    t.setheading(270)
    hopAlong(t, "+", 60, 60, 6, 1, 5)
    t.color("gray")
    t.setheading(0)
    hopAlong(t, "+", 60, 64.28571428571429, 7, 1, 5)
    t.color("darkgray")
    t.setheading(0)
    hopAlong(t, "+", 60, 67.5, 8, 1, 5)
    t.color("black")
    t.setheading(0)
    hopAlong(t, "+", 60, 70, 9, 1, 5)
    t.color("darkgray")
    t.setheading(0)
    hopAlong(t, "+", 60, 72, 10, 1, 5)


    t.penup()
    t.goto(-200,200)
    t.pendown()
    t.color("red")
    t.setheading(0)
    swingIt(t, "up", acceleration=-1, startSpeed=10)
    # swingIt(t, "up", radius=100, angle=90, count=10, acceleration=0, startSpeed=5):

    scr.exitonclick()
