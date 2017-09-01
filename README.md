# turtle-draw-remote
Run Python turtle module drawing commands remotely via web interface (i.e. smartphone "remote control")

"Remote Control" Drawing App

The issues I was "addressing" (more so than "solving" a problem):

1) Increase my CCV Web Dev. students' "awareness" of the various aspects of web apps (browser + server-side code, data store).
2) Entice students to later pursue another programming course (JavaScript, PHP, Java or Python).
3) Fun in-class activity at start of semester, where CCV students can begin to get to know each other.
4) Maker Faire: Entice younger kids to gain awareness and interest in programming / software development.

Notes:

The Website Development course's "Essential Objectives" primarily include HTML and CSS.  There are only slight mentions of app "behavior" or interactivity via JavaScript, and server-side code such as PHP.  Today's students think more in terms of web apps or apps, not merely static web pages (i.e. brochure-ware).  Learning to build web apps requires more than just one course at CCV.

My idea for this app originally came during the June 2016 CCV Summer Institute in the first morning's presentation and activity.  The workshop's theme was on how to engage student interest and participation via a variety of class activities, including games / game-ification.

I had previously taught the Python Programming course at CCV, which included Python Turtle drawing projects and assignments.  One homework assignment required students to programmatically read and parse an XML file of drawing commands and parameters, and then perform the correct drawing actions.  The students had to match a static drawing shown in the textbook.  My idea was that students could make drawings in near real-time, by a user clicking or pressing buttons on a "remote control" web interface.

This was initially developed for the Website Development course I taught at CCV-Rutland for an in-class activity.

In addition, the downtown Rutland Sidewalk Sale in August 2016 included the Rutland Mini Maker Faire.  I later demonstrated this app again at The Mint Makerspace Grand Opening on August 12, 2017.

The "remote control" interface can be run from smartphones.  Attendees can use their smartphones to draw with or animate their own Python "turtle".

I set the goal of completing the app in time for the 2016 Rutland Maker Faire, in order to more fully test the app components, and to also be ready for CCV course in September 2016.

The "remote control" app is multi-user: The users don't have to know about each other, but if they are standing or sitting near each other, it can be a fun and "competitive" activity (students, parents and kids).  "Competitive" is subjective, as their are "no rules", just an opportunity to "play" (draw, animate, play chase / tag)


Version 1: Most of the drawing related buttons features were developed prior to the Rutland Maker Faire in August 2016.

Version 2: A "Msg" feature was added a month later, so that users can send a message, and have their turtle write the message on Turtle canvas in their own color.


Summary of the application components:

4 programs (two clients, two server-side scripts)
2 asynchronous client/server apps
Shared data files of drawing commands (CSV format)
5 computer languages (HTML, CSS, JavaScript, PHP and Python)


Credits to students in Fall 2015 Python Programming course at CCV-Rutland:

Python modules for turtle spin, swing and shake movements: These modules were written by teams of Python Programming students in Fall 2015 during a "paired programming" exercise.  I included these code modules for some basic turtle moves into the Python app, which handle the buttons/commands for Spin (Left, Right), Bounce (Hop, Dip) and Shake (Horizontal, Vertical and Both).


Hosting this on your own web server:

If you wanted to host this on your own web server (localhost or otherwise), place these files in a directory ("turtle-draw-remote" or something else).  The HTML, CSS, JS, PHP and image files would run on web server.

The Python files would also be run separately as second client app, so they may need to be copied to another computer with Python 3 installation.  The turtle_draw_by_cmd.py file is the main Python file.  You can run from IDLE.

Before running you would need to tweak values for two variables in this function - "def getTurtleCmdQURL(cuttime):" (see line 216 and below).  Change "server" variable to URL for your web server domain.  For "cmdQPath" variable, the directory name would match where you put your project files on web server.

In a classroom situation or group setting, you can plug laptop or computer running Python app into a large screen or projector, then all can see all the drawing turtles at the same time.

There is a Help button on the remote control interface, which will explain to each remote user what to do.

On the Python display app (Turtle canvas), it is generally a single-user app (you).  So for speed I went with single keypress events, instead of GUI buttons (no need to find your mouse to "pause" polling requests, just press 'p' key).  Upon Python app startup, if you press 'p' to pause, you can then read the "menu" list of keypress commands.  Press 'p' again to "play".  Once the app resumes polling (PHP requests), you can use the remote control app (web interface).  There can be a slight delay depending on whether you are using cell tower or WiFi.  After you enter your "turtle" name and press "Start", you will be given a "color".  After the next GUI button you press, you should see your turtle, name and color magically appear on Python Turtle canvas.

It can feel like you are using a TV remote control (i.e. changing channels or volume).  But there is no "infrared" signal involved.  Just two hardworking PHP programs on the server to help navigate your drawing turtle!

Enjoy!

Ron

August 31, 2017
