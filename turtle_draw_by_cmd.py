import random
import time
import turtle
import datetime
import urllib.request

import CodyA_LucasB_KimberlyM_Spin as spin
import RonP_Swing as swing
import EliyahA_ScottF_Shake as shake

# turtle_draw_by_cmd.py
# Ron Pulcer (c) 2016

# Get To Do list of turtle commands.  The commands are sorted in time order and may be for multiple users.
# Repeat process continually until 'x' key is pressed to exit app.
# Process each drawing command record in order to draw or animate the respective turtle object.
# Keep track of cutoff time and pass this time param in PHP request to get "next" command(s).
# When reading the PHP response, the first record lists number of users and commands.
# This is FYI, so the first actual command to process is row 2.

# There are several key press events:
# 'c' for clearing the Turtle canvas
# 'd' for debug mode (output appears on console screen)
# 'p' for Pause / Play (resume) of processing drawing commands
# 'r' for reboot of Turtle canvas; similar to 'c' for clear,
#     but also includes rewriting heading and animation at top of screen.
# 'x' for Exit of app.

# Example request
# http://localhost/rmf/get_turtle_cmd_queue.php?cutoff_time=2016-07-15+17:30:15+EDT

# 2016 July: Initial development of Python drawing display app.


# Setup key press events and optionally prints menu information
def setupMenu(printOption):
    global tScreen
    tScreen.onkeypress(clearTurtleDrawings, "c")
    tScreen.onkeypress(toggleDebugMode, "d")
    tScreen.onkeypress(togglePlayPause, "p")
    tScreen.onkeypress(rebootTurtleScreen, "r")
    tScreen.onkeypress(signalExit, "x")

    tScreen.listen()

    if printOption:
        print("Menu of key-press commands:")
        print("Press 'c' to clear Turtle drawings (turtles can resume drawing from current location)")
        print("Press 'd' to toggle Debug Mode (currently OFF)")
        print("Press 'p' to toggle Play / Pause mode (currently in Pause mode)")
        print("Press 'r' to 'reboot' Turtle Screen (both drawings and turtles cleared)")
        print("Press 'x' to request the program to Exit\n")


# Handle common params for any command
def setParams(turt, spd, pen):
    turt.speed(spd)
    if(pen == "true"):
        turt.pendown()
    else:
        turt.penup()


# Handle directional commands
def goDirection(turt, dir, turn, stp):
    if dir == "northwest" and turn == "true":
        turt.setheading(135)
    elif dir == "north" and turn == "true":
        turt.setheading(90)
    elif dir == "northeast" and turn == "true":
        turt.setheading(45)
    elif dir == "east" and turn == "true":
        turt.setheading(0)
    elif dir == "southeast" and turn == "true":
        turt.setheading(315)
    elif dir == "south" and turn == "true":
        turt.setheading(270)
    elif dir == "southwest" and turn == "true":
        turt.setheading(225)
    elif dir == "west" and turn == "true":
        turt.setheading(180)

    turt.forward(stp)


# Handle drawing of polygons
def makePolygon(turt, shape, fill, stp):
    sides = 1
    if shape == "triangle":
        sides = 3
    elif shape == "square":
        sides = 4
    elif shape == "pentagon":
        sides = 5
    elif shape == "hexagon":
        sides = 6
    elif shape == "septagon":
        sides = 7
    elif shape == "octagon":
        sides = 8
    elif shape == "nonagon":
        sides = 9

    if fill == "true":
        turt.begin_fill()

    angle = 360 / sides
    for s in range(sides):
        turt.left(angle)
        turt.forward(stp)

    if fill == "true":
        turt.end_fill()


# Handle 'p' key press event
def togglePlayPause():
    global togglePlay

    if togglePlay:
        togglePlay = False
        print('-' * 50)
        print("Begin Pause ... press 'p' key to resume play.")
        print('-' * 50)
    else:
        togglePlay = True
        print('-' * 50)
        print("Begin / resume Play ... press 'p' key to pause.")
        print('-' * 50)


# Handle 'd' key press event
def toggleDebugMode():
    global toggleDebug

    if toggleDebug:
        toggleDebug = False
        print('-' * 50)
        print("Debug mode turned OFF ... press 'd' key to turn on.")
        print('-' * 50)
    else:
        toggleDebug = True
        print('-' * 50)
        print("Debug mode turned ON ... press 'd' key to turn off.")


# Handle 'c' key press event
def clearTurtleDrawings():
    # Clear each turtle's drawing, but retain the turtle references / properties
    print('-' * 50)
    print("clearTurtleDrawings")
    print('-' * 50)
    global turtleDict, name
    for k in turtleDict.keys():
        turt = turtleDict[k]
        if turt != None:
            turt.write("Shaking like Etch-a-Sketch!", align="left", font=("Arial", 14, "bold"))
            shake.shakeItUp(turt, direction="random", count=random.randint(5, 10))
            turt.clear()
            turt.write(name, align="left", font=("Arial", 20, "normal"))


# Handle 'r' key press event
def rebootTurtleScreen():
    # Clear out turtle dictionary and clear screen drawings
    print('-' * 50)
    print("Rebooting Turtle Screen!")
    print('-' * 50)
    global turtleDict, tScreen, rmf_turtle
    turtleDict = {}
    tScreen.clear()
    rmf_turtle = turtle.Turtle()
    makerFaireIntro(rmf_turtle)
    setupMenu(False)
    

# Handle 'x' key press event
def signalExit():
    global togglePlay

    # Confirm exit?
    togglePlay = False
    print("Exit requested: Program will close after housekeeping...")
    # houseKeeping()
    exit()
        

# Write the heading text at top of screen and do initial animation
def makerFaireIntro(turt):
    turt.color("green")
    turt.shape("turtle")
    turt.penup()
    turt.pencolor("#00CCFF")
    turt.goto(-160, 275)
    # turt.pendown()
    turt.write("Welcome to Rutland Maker Faire", align="left", font=("Arial", 12, "bold"))
    turt.pencolor("#FF0000")
    turt.goto(-260, 250)
    turt.write("Turtle Drawing via Remote Control Commands", align="left", font=("Arial", 14, "bold"))
    turt.goto(0, 240)


# For debugging only, get a list of commands to test
def getTestFile():
    # datadir = "C:\\wamp\\www\\rmf\\"
    datadir = ".\\"

    # testFile = "Ronald_E67A3E_commands.txt"
    # testFile = "RonP_44D4BE_commands_draw.txt"
    # testFile = "testing123_EEEE44_commands_animate.txt"
    testFile = "testing123_EEEE44_commands_draw.txt"
    return datadir + testFile


# Build URL for PHP request to get To Do List of drawing commands (queue) based on cutoff time
def getTurtleCmdQURL(cuttime):
    # The first replace (T) are not necessary if the input param already has "T" between date and time.
    # cuttime = cuttime.replace(" ", "T", 1)
    cuttime = cuttime.replace(" ", "+", 1)

    # server = "http://localhost/"
    # server = "http://ronpulcer.com/"
    server = "http://rxp08190.classweb.ccv.edu/"

    # cmdQPath = "rmf/data/RonP_44D4BE_commands.txt"
    # cmdQPath = "rmf/data/RonP_44D4BE_commands.txt"
    # cmdQPath = "rmf/get_turtle_cmd_queue.php?cutoff_time=" + cuttime
    # cmdQPath = "mintgo/get_turtle_cmd_queue.php?cutoff_time=" + cuttime
    # cmdQPath = "Middlebury/get_turtle_cmd_queue.php?cutoff_time=" + cuttime
    cmdQPath = "turtle-draw-remote/get_turtle_cmd_queue.php?cutoff_time=" + cuttime

    cmdQUrl = server + cmdQPath

    if toggleDebug:
        print("HTTP request path:", cmdQPath)
    print("HTTP request URL:", cmdQUrl)

    return cmdQUrl


# Make PHP request using URL param to get To Do List of drawing commands (queue)
def getTurtleCmdQueue(url):
    # if toggleDebug: print("URL param:", url)
    turtleToDo = ""
    commandList = []

    resp = urllib.request.urlopen(cmdQUrl)
    turtleToDo = str(resp.readall().decode("utf-8"))
    if toggleDebug: print(turtleToDo)

    commandList = turtleToDo.split("\n")
    if toggleDebug: 
        print(commandList)
        print(type(commandList))
        print("Len: ", len(commandList))

    return commandList


# Handle the spinning turtle at top of screen
def spinTimer():
    # In lieu of using the time.sleep() or letting "while True" run wild (which hangs up Turtle Screen),
    # this is an attempt to provide some "eye candy" for user (spinning turtle at top of screen),
    # but also keep the Turtle Screen somewhat busy for a moment before doing next HTTP request (a "throttle")
    global rmf_turtle
    randDir = random.randint(0, 100) % 2
    randCnt = random.randint(0, 2) + 1
    if randDir == 0:
        spin.rotate(rmf_turtle, "left", randCnt)
    else:
        spin.rotate(rmf_turtle, "right", randCnt)


# Main process
if __name__ == "__main__":

    # Draw introductory Rutland Maker Faire logo!
    rmf_turtle = turtle.Turtle()
    tScreen = rmf_turtle.getscreen()

    makerFaireIntro(rmf_turtle)

    # The "p" key is for toggling Play/Pause (True/False)
    # Begin in Pause mode, so that PHP web requests are not run until "remote control" user(s) are ready
    # The "d" key is for toggling Debug mode (True/False)
    # The "x" key is for exiting program

    togglePlay  = True
    # togglePlay  = False
    toggleDebug = False

    setupMenu(True)

    # Remote user turtles will be stored by First Name + Color
    turtleDict = {}

    idxTmStamp = 0
    idxName    = 1
    idxColor   = 2
    idxCmd     = 3
    idxParam   = 4
    idxSpeed   = 5
    idxStep    = 6
    idxPenDown = 7

    
    # Read commands from local file:
    # testFile = getTestFile()
    # turtleToDo = open(testFile, "r", encoding="utf-8-sig")

    # ttdLine = turtleToDo.readline().strip()
    # print(ttdLine)

    # cutoff_time will be in "YYYY-MM-DDThh:mm:ss TZn" format (i.e."2016-07-27T00:00:00 EDT")
    timenow = datetime.datetime.now()
    print(timenow.isoformat(sep=" "))
    cutoff_time = timenow.isoformat(sep=" ")[0:19] + " EDT"
    # Put a "T" between date and time, otherwise via Python, the HTTP request acts as if param is YYYY-MM-DD 00:00:00 (midnight)
    cutoff_time = cutoff_time.replace(" ", "T", 1)
    print("Cutoff time (NOW):", cutoff_time)

    # For testing only: override cutoff_time
    # cutoff_time = "2016-07-29T04:11:00 EDT"
    # cutoff_time = "2016-07-27T00:00:00 EDT"
    # cutoff_time = "2016-07-29T08:00:00 EDT"
    print("Cutoff time override:", cutoff_time)

    # Infinite loop ... until 'x' pressed to Exit (or some other brute force method!)
    while True:

        if not togglePlay:
            # In lieu of using the time.sleep() or letting "while True" run wild (which hangs up Turtle Screen),
            # this is an attempt to provide some "eye candy" for user (spinning turtle at top of screen),
            # but also keep the Turtle Screen somewhat busy for a moment before doing next HTTP request (a "throttle")
            spinTimer()
        else:

            # print("Sleeping 1 seconds...")
            # time.sleep(1)
            spinTimer()

            # Read commands from the web:
            cmdList = []
            turtleToDo = ""
            cmdQUrl = getTurtleCmdQURL(cutoff_time)
            cmdList = getTurtleCmdQueue(cmdQUrl)

            ttdLine = ""

            # First row in cmdList is summary of users and commmands.  Also, last row is blank after the last \n.
            # Users: #, Commands: #
            if len(cmdList) > 0:
                summaryLine = cmdList.pop(0).strip()
                print(summaryLine)

                if toggleDebug: print("# Commands:", len(cmdList))

                if len(cmdList) > 0:
                    ttdLine = cmdList.pop(0).strip()

                while ttdLine != "":
                    if toggleDebug: print(ttdLine)
                    print("# Commands:", len(cmdList))

                    # With new "message" command, there could be embedded comma in message,
                    # so switching delmiter to pipe char "|"
                    rec = ttdLine.split("|")

                    tmStamp = rec[idxTmStamp]
                    name    = rec[idxName]
                    color   = rec[idxColor]
                    cmd     = rec[idxCmd]
                    param   = rec[idxParam]
                    speed   = rec[idxSpeed]
                    step    = rec[idxStep]
                    penDown = rec[idxPenDown]

                    if toggleDebug:
                        print(rec)
                        print("Timestamp = %s" % rec[idxTmStamp])
                        print("Name      = %s" % rec[idxName])
                        print("Color     = %s" % rec[idxColor])
                        print("Cmd       = %s" % rec[idxCmd])
                        print("Param     = %s" % rec[idxParam])
                        print("Speed     = %s" % rec[idxSpeed])
                        print("Step      = %s" % rec[idxStep])
                        print("PenDown   = %s" % rec[idxPenDown])
                        print("")

                    # Put latest timestamp into cutoff_time in preparation for next command queue request
                    cutoff_time = tmStamp.replace(" ", "T", 1)
                    # if toggleDebug:
                    print("Next cutoff_time:", cutoff_time)

                    # Turtle dictionary key is name + color
                    # print(len(turtleDict))
                    tKey = name + "_" + color
                    tName = turtleDict.get(tKey)
                    print(tKey, cmd)
                    if toggleDebug: print("tName:", tName)

                    if tName == None:
                        tName = turtle.Turtle()
                        turtleDict[tKey] = tName
                        if toggleDebug: print("New turtle:", tKey, tName)

                        tName.shape("turtle")
                        tName.color(color)
                        tName.penup()

                        # Random positioning of turtle before writing turtle name
                        # Leave some room around edges for turtle to move around
                        
                        randX = random.randint(0, tScreen.window_width() // 2)  * 0.5
                        randY = random.randint(0, tScreen.window_height() // 2) * 0.5
                        randSignX = (random.randint(0, 100) % 2) * 2 - 1
                        randSignY = (random.randint(0, 100) % 2) * 2 - 1
                        # print("randX = ", randX)
                        # print("randY = ", randY)
                        # print("randSignX = ", randSignX)
                        # print("randSignY = ", randSignY)
                        tName.goto(randX * randSignX, randY * randSignY)
                        
                        tName.write(name, align="left", font=("Arial", 20, "normal"))

                    
                    setParams(tName, int(speed), penDown)

                    if cmd == "north" or cmd == "south" or cmd == "east" or cmd == "west":
                        goDirection(tName, cmd, param, int(step))

                    elif cmd == "northwest" or cmd == "southwest" or cmd == "northeast" or cmd == "southeast":
                        goDirection(tName, cmd, param, int(step))

                    elif cmd == "center":
                        tName.goto(0,0)

                    elif cmd == "spinleft":
                        spin.rotate(tName, "left", count=int(param))
                    elif cmd == "spinright":
                        spin.rotate(tName, "right", count=int(param))

                    elif cmd == "hop":
                        tName.setheading(270)
                        swing.hopAlong(tName, direction="up", radius=int(step), count=int(param))
                    elif cmd == "dip":
                        tName.setheading(90)
                        swing.hopAlong(tName, direction="down", radius=int(step), count=int(param))

                    elif cmd == "shakehoriz":
                        shake.shakeItUp(tName, direction="horizontal", count=random.randint(5, 10))
                    elif cmd == "shakevert":
                        shake.shakeItUp(tName, direction="vertical", count=random.randint(5, 10))
                    elif cmd == "shakeboth":
                        shake.shakeItUp(tName, direction="random", count=random.randint(5, 10))

                    elif cmd == "circle":
                        if param == "true":
                            tName.begin_fill()

                        tName.circle(int(step))

                        if param == "true":
                            tName.end_fill()

                    elif cmd == "triangle" or cmd == "square" or cmd == "pentagon" or cmd == "hexagon" or cmd == "septagon" or cmd == "octagon" or cmd == "nonagon":
                        makePolygon(tName, cmd, param, int(step))

                    elif cmd == "message":
                        tName.write(param, align="left", font=("Arial", 14, "normal"))

                    # This clears an individual turtle's drawing (remote user control)
                    # The 'c' onkey event allows the Python app user to clear a turtle's drawing
                    elif cmd == "clear":
                        tName.write("Shaking like Etch-a-Sketch!", align="left", font=("Arial", 14, "bold"))
                        shake.shakeItUp(tName, direction="random", count=random.randint(5, 10))
                        tName.clear()
                        tName.write(name, align="left", font=("Arial", 20, "normal"))

                    elif cmd == "stop":
                        tName.write(name + " signing off ... Bye Bye!", align="left", font=("Arial", 20, "italic"))
                        time.sleep(2)
                        tName.setheading(270)
                        tName.forward(30)
                        tName.write("Shaking like Etch-a-Sketch!", align="left", font=("Arial", 16, "bold"))
                        shake.shakeItUp(tName, direction="random", count=random.randint(5, 10))
                        tName.clear()
                        tName.hideturtle
                        turtleDict[tKey] = None
                      
                        
                    if toggleDebug: print('-' * 50)
                    # time.sleep(1)

                    # Local file or test file:
                    # ttdLine = turtleToDo.readline().rstrip()

                    # Web request with cutoff time
                    if len(cmdList) > 0:
                        ttdLine = cmdList.pop(0).strip()
                    else:
                        ttdLine = ""


# Local file:
# turtleToDo.close()

tScreen.exitonclick()
