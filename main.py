import turtle as trtl
import random as rand
#Set up variables
wn = trtl.Screen()
maze_maker = trtl.Turtle()
maze_maker.goto(0, 0)
maze_maker.speed(0)
maze_maker.left(90)
maze_maker.pensize(5)
numlines = 0
line_length = 50
door_size = 30
before_door = 20
block_size = 40
randmin = 10
randmax = 50
#Draw the maze
while(numlines <= 24):
    if (numlines < 6):
        maze_maker.forward(line_length)
    else:
        before_door = rand.randint(randmin, randmax)
        if (before_door == )
        maze_maker.forward(before_door)
        maze_maker.penup()
        maze_maker.forward(door_size)
        maze_maker.pendown()
        #barriers
        maze_maker.forward(before_door * 2.5)
        maze_maker.right(90)
        maze_maker.forward(block_size)
        maze_maker.right(180)
        maze_maker.forward(block_size)
        maze_maker.right(90)
        maze_maker.forward(line_length - door_size - before_door - before_door * 2.5)
    maze_maker.right(90)
    line_length += 20
    numlines += 1


wn.listen()
wn.mainloop()

"""
def spot_clicked(x, y):
    t.goto(rand.randint(xmin, xmax), rand.randint(ymin, ymax))
    scorechange()
    addcolor()
    sizechanger()

def addcolor():
    colorlist = ["black", "blue", "green", "yellow", "lime", "orange", "purple"]
    t.fillcolor(rand.choice(colorlist))
    t.stamp()
    t.fillcolor(color)

def sizechanger():
    sizechange = [0.5, 1, 2, 3, 4, 2.5, 4.8]
    t.turtlesize(rand.choice(sizechange))
"""