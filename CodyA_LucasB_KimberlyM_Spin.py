import turtle

#Project Spinny by Cody Adams, Lucas Billings, Kimberly Madison
#11/11/15
#PROJECT SPINNY: turtles got moves

# NOTE: Moving the creation of turtle to "main" section
# t = turtle.Turtle()
# screen = t.getscreen()
# t.shape("turtle")

def spinLeft(turt):
    turt.left(360)


def spinRight(turt):
    turt.right(360)


def rotate(turt, direction="right", count=3, acceleration=0, startSpeed=5):
    direction = direction.lower()
    #t.speed(startSpeed)
    turt.speed(startSpeed)
    for x in range(count):
        if direction == "left" or direction == "counterclockwise" or direction == "-":
            #spinLeft(t)
            spinLeft(turt)
        elif direction == "right" or direction == "clockwise" or direction == "+":
            #spinRight(t)
            spinRight(turt)
        #t.speed(t.speed() + acceleration)
        turt.speed(turt.speed() + acceleration)
        
if __name__ == "__main__":

    t = turtle.Turtle()
    screen = t.getscreen()
    t.shape("turtle")

    spinLeft(t)
    spinRight(t)
    rotate(t, "right" ,5, -2, 10)
    screen.exitonclick()



