# Imports
import turtle as trtl
import random as rand

#Setup Variables
numSides = 25
length = 20
color = "black"
doorSize = 40
beforeDoor = 5

#Turtle Settings
painter = trtl.Turtle()
painter.pencolor(color)
painter.speed("fastest")
painter.pensize(5)


currentSide = 0
currentSize = length
preBarrier = 40

while(currentSide < numSides):
    if(currentSide < 4):
        #painter.forward(currentSize)
        print("Bruh")
    else:
        beforeDoor = rand.randint(length, currentSize - doorSize-length)
        prebarrier = rand.randint(length, currentSize - length beforeDoor)

        if(beforeDoor < prebarrier):

            # Door Handle(r)
            painter.forward(beforeDoor)
            #painter.penup()
            painter.pencolor("red")
            painter.forward(doorSize)
            painter.pencolor(color)
            #painter.pendown()

            # CFM Code Here
            painter.forward(preBarrier)
            painter.left(90)
            painter.forward(length*2)
            painter.right(180)
            painter.forward(length*2)
            painter.left(90)
            # Wall End

        elif(beforeDoor > prebarrier):

            # CFM Code Here
            painter.forward(beforeDoor)
            painter.left(90)
            painter.forward(length * 2)
            painter.right(180)
            painter.forward(length * 2)
            painter.left(90)
            # Wall End

            # Door Handle(r)
            painter.forward(prebarrier)
            # painter.penup()
            painter.pencolor("red")
            painter.forward(doorSize)
            painter.pencolor(color)
            # painter.pendown()







        else:

            prebarrier = 40
            beforeDoor = length * 2
            # Door Handle(r)
            painter.forward(beforeDoor)
            # painter.penup()
            painter.pencolor("red")
            painter.forward(doorSize)
            painter.pencolor(color)
            # painter.pendown()

            # CFM Code Here
            painter.forward(preBarrier)
            painter.left(90)
            painter.forward(length * 2)
            painter.right(180)
            painter.forward(length * 2)
            painter.left(90)
            # Wall End


        painter.forward(currentSize - doorSize - beforeDoor - preBarrier)

    painter.left(90)
    currentSize += length
    currentSide+=1

painter.hideturtle()

wn = trtl.Screen()
wn.mainloop()