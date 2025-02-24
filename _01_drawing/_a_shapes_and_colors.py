import turtle


window = turtle.Screen()
window.bgcolor('white')

# This code makes a new Turtle. Pick a new name for the turtle
my_pycharm = turtle.Turtle()



# Make your turtle's shape 'turtle', .shape('turtle')
my_pycharm.shape("turtle")


# Set your turtle's speed using .speed(2)
my_pycharm.speed(2)
# Set your turtle's color using .color('green') and .pencolor('blue')
my_pycharm.color('green')
my_pycharm.pencolor ('blue')

# Move your turtle forward using .forward(100)
my_pycharm.forward(100)
# TEST    Did your turtle move forward?

# Move your turtle left or right using .left(90) or .right(90)
my_pycharm.left(90)

# Now put the forward and left/right code into a for loop to repeat 4 times.
for i in range (4):
    my_pycharm.forward(100)
    my_pycharm.left(90)
# TEST    Did your turtle draw a square?

# Move your turtle to a new place on the screen using .goto(x, y)
my_pycharm.goto(7,11)
# x=0 and y=0 is the center of the screen
my_pycharm.begin_fill()
# Have your turtle draw a circle using .circle(radius, steps=30)
my_pycharm.circle(15,steps=30)
# TEST    Did your turtle draw a circle?

# Add color to your shape by adding .begin_fill() before drawing the circle
# and .end_fill() below
my_pycharm.end_fill()

# Draw 3 more shapes with different fill colors!
my_pycharm.color('blue')
my_pycharm.begin_fill()
my_pycharm.circle(45,steps=30)
my_pycharm.end_fill()


my_pycharm.color('purple')
my_pycharm.begin_fill()
my_pycharm.circle(90,steps=60)
my_pycharm.end_fill()

# ===================== DO NOT EDIT THE CODE BELOW ============================
turtle.done()
