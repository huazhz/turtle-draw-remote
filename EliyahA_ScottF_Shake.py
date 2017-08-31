import turtle
import random
##Penned By Eliyah and Scott
## Lords unmatched
def shakeHorizontal(tortName, xcor): ## thus wert a definition
    scr = tortName.getscreen()
    tortName.penup()
    #for shakes in range(400):
    for shakes in range(10):
       # scr.tracer(0)
        tortName.goto(random.randrange((-1*xcor),xcor),tortName.ycor())
        scr.tracer(1)

#NOTE: If you use forward() and/or backward() instead of goto() then you could have shake go in same direction turtle is heading.
# Or, you could include a new param (syncHeading=True boolean), and make it an option (either forward+backward or goto).
# That could apply to next 2 functions, just a thought!
def shakeVertical(tortName, ycor): ## thus wert a definition
    scr = tortName.getscreen()
    tortName.penup()
    #for shakes in range(400):
    for shakes in range(10):
      #  scr.tracer(0)
        tortName.goto(tortName.xcor(), random.randrange((-1*ycor),ycor))
        scr.tracer(1)
def shakeRandom(tName, xRange, yRange):
    scr = tName.getscreen()
    tName.penup()
    #for shakes in range(400):
    for shakes in range(10):
        tName.goto(random.randrange((-1*xRange),xRange),random.randrange((-1*yRange),yRange))

#def shakeItUp(tName, direction, count,acc,startSpeed):
def shakeItUp(tName, direction="horizontal", count=10, acceleration=0, startSpeed=5):
#NOTE: We "could" add a param for WIDTH of shake (after the direction) if you want more user (programmer) control!
    tName.penup()
    scr = tName.getscreen()
    #xRange = random.randrange(1,600)
    ##yRange = random.randRange(1,600)
    #yRange = random.randrange(1,600)
    xRange = random.randrange(1,20)
    yRange = random.randrange(1,20)
    #NOTE: Since all for loops are the same, you could consolidate to one (1) for loop with if-elif inside!
    if direction == "random":
        for shakes in range(count):
            shakeRandom(tName, xRange, yRange)
    elif direction == "horizontal":
        for shakes in range(count):
            shakeHorizontal(tName, xRange)
    elif direction == "vertical":
        for shakes in range(count):
            shakeVertical(tName, yRange)
    elif direction == "north":
        for shakes in range(count):
            tName.seth(90)
            tName.forward(xRange)
    elif direction == "south":
        for shakes in range(count):
            tName.seth(270)
            tName.forward(xRange)
    elif direction == "west":
        for shakes in range(count):
            tName.seth(180)
            tName.forward(xRange)
    elif direction == "east":
        for shakes in range(count):
            tName.seth(0)
            tName.forward(xRange)  

# Added this line of code so would not always run from importing programs
if __name__ == "__main__":
    
    billyBob = turtle.Turtle()
    #tompson = turtle.Turtle()
    screen = billyBob.getscreen()
    #tomscreen = tompson.getscreen()

    #cyberman = "cyberman.gif"
    #jarjar = "jarjar.gif"
    #screen.addshape(cyberman)
    #tomscreen.addshape(jarjar)
    #billyBob.shape(cyberman)
    #tompson.shape(jarjar)

    #tompson.goto(-300,-300)

    #shakeItUp(billyBob,"north",4,)

    shakeHorizontal(billyBob,30)
    shakeVertical(billyBob,50)

    shakeItUp(billyBob)
    billyBob.seth(45)
    shakeItUp(billyBob)

    # NOTE: Behavior for N,S,E,W is additive forwards instead of shaking (back and forth)
    shakeItUp(billyBob, "north")
    shakeItUp(billyBob, "south")
    shakeItUp(billyBob, "east")
    shakeItUp(billyBob, "west")

    #NOTE: acceleration and startSpeed not implemented yet (coming soon...)
    shakeItUp(billyBob, "horizontal", 10, 1, 1)
    shakeItUp(billyBob, "vertical", 10, -1, 10)




    billyBob.getscreen().exitonclick()

