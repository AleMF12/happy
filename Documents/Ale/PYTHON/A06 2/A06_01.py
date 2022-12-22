import turtle

t = turtle.Turtle()
t.speed('fast')

### YOUR CODE STARTS HERE

### YOUR CODE ENDS HERE

ts = turtle.getscreen()
ts.getcanvas().postscript(file="my-drawing.eps")

t.screen.mainloop()