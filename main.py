import turtle as trtl
#Set up variables
wn = trtl.Screen()
maze_maker = trtl.Turtle()
maze_maker.goto(0, 0)
maze_maker.speed(0)
maze_maker.left(90)
maze_maker.pensize(3)
numlines = 0
line_length = 30
#Draw the maze
while(numlines <= 25):
    maze_maker.forward(line_length)
    maze_maker.right(90)
    line_length += 10
    numlines += 1







wn.listen()
wn.mainloop()