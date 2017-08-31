import turtle

# NOTE: Moved these below for the "main" section
#t = turtle.Turtle()
#scr = t.getscreen()

def jump(turt, x):
    turt.setheading (90)
    turt.forward (x)
    turt.backward (x)
    
    
    
    
#def dip(turtle, x):
def dip(turt, x):
    #t.setheading (-90)
    #t.forward (x)
    #t.backward (x)
    turt.setheading (-90)
    turt.forward (x)
    turt.backward (x)
    
def bounce(turtle, direction="up", count=3, acceleration=0, startSpeed=5, startHeight=0, subtractHeight=-5):
    jump (t, 200)
    dip (t, 200)

    
if __name__ == "__main__":
    
    t = turtle.Turtle()
    scr = t.getscreen()

    t.speed (1)
    # Added these two test cases
    jump (t, 200)
    dip (t, 200)

    bounce (t, 200)
   
    scr.exitonclick()
