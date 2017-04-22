#setup
from turtle import *
import random
#colours to chose from
speed('fastest')
hideturtle()
def color_1():
    pencolor("#ff0000")
def color_2():
    pencolor("#a80000")
def color_3():
    pencolor("#ff4242")
def color_4():
    pencolor("#ffc9c9")
def colors():
    colorFunction=random.randint(0,3)
    if colorFunction == 0:
        color_1()
    elif colorFunction == 1:
        color_2()
    elif colorFunction == 2:
        color_3()
    else:
        color_4()
#start of program
penup()
goto(100,100)
pendown()
for a in range(100):
    for b in range(100):
        colors()
        fd(1)
    penup()
    goto(100,100 - a - 1)
    pendown()
    
    
    
#setup
from turtle import *
import random
#colours to chose from
speed('fastest')
hideturtle()
def color_1():
    pencolor("#ff0000")
def color_2():
    pencolor("#a80000")
def color_3():
    pencolor("#ff4242")
def color_4():
    pencolor("#ffc9c9")
def colors():
    colorFunction=random.randint(0,3)
    if colorFunction == 0:
        color_1()
    elif colorFunction == 1:
        color_2()
    elif colorFunction == 2:
        color_3()
    else:
        color_4()
#start of program
penup()
goto(200,200)
pendown()
for a in range(0,200,2):
    for b in range(0,200,2):
        xval = xcor()
        yval = ycor()
        colors()
        fd(2)
        penup()
        goto(xval,yval - 1)
        pendown()
        fd(2)
        penup()
        goto(xval + 2,yval)
        pendown()
    penup()
    goto(200,200 - a - 2)
    pendown()




from turtle import *
import random
sides=int(input("how many sides? "))
def randomAngle():
    angle=random.randint(1,179)
    if left_or_right == 2:
        mode = 2

for i in range(sides - 1):
    angle = randomAngle()
    if mode == 2:
        left_or_right = 1
    else:
        left_or_right = random.randint(1,2)
    length=random.randint(0,100)
    fd(length)
    if left_or_right == 1:
        rt(angle)
    else:
        lt(angle)
goto(0,0)



from turtle import *
colormode(255)
import random, math
hideturtle()
while 1:
    away = random.randint(0,100)
    angle = random.randint(0,360)
    goto(math.cos(angle)*away,math.sin(angle)*away)
    full = 255
    r = random.randint(0, full)
    g = random.randint(0, full)
    b = random.randint(0, full)
    pencolor(r, g, b)



from turtle import *
colormode(255)
import random, math
hideturtle()
while 1:
    goto(random.randint(-100,100),random.randint(-100,100))
    full = 255
    r = random.randint(0, full)
    g = random.randint(0, full)
    b = random.randint(0, full)
    pencolor(r, g, b)
