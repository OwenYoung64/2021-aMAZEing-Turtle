import turtle as trtl
#Set up variables
wn = trtl.Screen()
maze_maker = trtl.Turtle()
maze_maker.goto(0, 0)
maze_maker.speed(0)
maze_maker.left(90)
number_of_lines = 0
line_length = 30
#Draw the maze
while(number_of_lines <= 25):
    maze_maker.forward(line_length)
    maze_maker.right(90)
    line_length += 10
    number_of_lines += 1








wn.listen()
wn.mainloop()