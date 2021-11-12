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
#Draw the maze
while(numlines <= 24):
    if (numlines < 6):
        maze_maker.forward(line_length)
    else:
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