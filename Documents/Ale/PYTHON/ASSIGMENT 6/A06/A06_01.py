import turtle
t = turtle.Turtle()
t.speed('fast')

### YOUR CODE STARTS HERE
# In this part I defined the background of the screen.
screen = turtle.Screen()
screen.bgcolor("pink")

# THE BASE OF CHURCH 1
# Here I created the base of the church. First, I defined the pencolor, the filling color of the square
# and pensize. Then I used the drawing methods forward, right ,left and fill color and so on.
# To draw and color the base of the church.

t.pen(pencolor="black", fillcolor="orange", pensize=2)
t.begin_fill()
t.right(90),
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.right(90)
t.end_fill()

# THE BASE OF CHURCH 2
# This part is basically the same of the base 1 church in the 4th quadrant that is parallel to the base 1.
# So, first I defined the pencolor, the filling color of the square and pensize. Then I used the drawing
# methods forward, right ,left and fill color to draw the four sides of the square and color the base of the church.

t.pen(pencolor="black", fillcolor="orange", pensize=2)
t.begin_fill()
t.left(-90)
t.forward(-200)
t.right(-90)
t.forward(-150)
t.right(-90)
t.forward(-200)
t.right(-90)
t.forward(-150)
t.end_fill()

#THE DOOR OF THE CHURCH
#Here for the door I drew a rectangle that will be the door of the church. To begin I used the turtle object and from it
# I used the method penup to move to another point without writing, then to write again I use pen down. I also used turtle
#pen to set the pen color, fill color and pensize.
t.penup()
t.goto(-45,-150)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", fillcolor="brown", pensize=2)
t.begin_fill()
t.left(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.end_fill()
t.penup()

#TRIANGLE ROOF
#I decided to draw for the church a triangule roof. I used the drawing methods. penup,pendown,forward,left and so on.
#Here again the pen function helped me to set the pen color black,pensize and filling color.

t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", fillcolor="brown", pensize=2)
t.begin_fill()
t.forward(90)
t.left(120)
t.forward(180)
t.left(-240)
t.forward(180)
t.right(-120)
t.forward(180)
t.end_fill()
t.penup()


#SQUARE ROOF
#I decided to add the name of the church so I created a rectangular roof and on it I added the name of the church.
# I used the drawing methods. penup,pendown,forward,left and so on. #Here again the pen function helped me to set
# the pen color black,pensize and filling color.

t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", fillcolor="white", pensize=3)
t.begin_fill()
t.forward(170)
t.left(90)
t.forward(40)
t.left(90)
t.forward(340)
t.left(90)
t.forward(40)
t.left(90)
t.forward(170)
t.end_fill()
t.penup()

#CHURCHS NAME
#In this section I used the write function to write the name of the church.
#I defined also the font; the type of the letter,the size and bold.
t.penup()
t.goto(-90,10)
t.setheading(0)
t.pendown()
t.write("HANDONG CHURCH", font=("Batang",15,"bold"))
t.penup()


#THE CROSS
#In the top of the roof I decided to put the cross. Here I use for loop to create it.
#the range of the loop is 4 and the lenght of the sides of the cross are equivalent to 10.

t.pen(pencolor="black", fillcolor="brown", pensize=2, speed=9)
t.color('black')
t.up()
t.goto(-15,150)
t.down()
t.begin_fill()
for _ in range(4):
    t.fd(10)
    t.right(90)
    t.fd(10)
    t.left(90)
    t.fd(10)
    t.left(90)
t.end_fill()
t.penup()

# ROUND WINDOW.
# I drew circular windows. I used the circle function that defines the diameter.
#The diameter is 20 and the filling color is yellow.
t.penup()
t.goto(-140,-80)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", fillcolor="yellow", pensize=2, speed=9)
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()

#LINES ON THE WINDOW
#I drew a vertical and horizontal straight line in the window from up to down
#and from left to right to make it look more like a traditional window.
t.penup()
t.goto(-140,-80)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", pensize=3)
t.begin_fill()
t.left(90)
t.forward(40)
t.end_fill()
t.pendown()

t.penup()
t.goto(-160,-60)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", pensize=3)
t.begin_fill()
t.forward(40)
t.end_fill()
t.pendown()

# ROUND WINDOW 2
# I drew the second circular window in the fourth quadrant that is parallel to the first window.
# I used the circle function that defines the diameter of the circle.
#The diameter is 20 and the filling color is yellow.
t.penup()
t.goto(140,-80)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", fillcolor="yellow", pensize=2)
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()

#LINES ON THE WINDOW 2
# In the same way as the first I drew a vertical and horizontal straight line in the window from up to down
# and from right to left to make it look more like a traditional window. I used the
t.penup()
t.goto(140,-80)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", pensize=3)
t.begin_fill()
t.left(90)
t.forward(40)
t.end_fill()
t.pendown()

t.penup()
t.goto(160,-60)
t.setheading(0)
t.pendown()
t.pen(pencolor="black", pensize=3)
t.begin_fill()
t.left(180)
t.forward(40)
t.end_fill()
t.pendown()

#MY NAME
#Finally I used the write function to write my name on the drawing. I used font; magneto, size 11 and bold
t.penup()
t.goto(10,-250)
t.setheading(0)
t.pendown()
t.write("Alejandra Mollo Flores", font=("Magneto",15,"bold"))
t.penup()


### YOUR CODE ENDS HERE

ts = turtle.getscreen()
ts.getcanvas().postscript(file="my-drawing.eps")

t.screen.mainloop()