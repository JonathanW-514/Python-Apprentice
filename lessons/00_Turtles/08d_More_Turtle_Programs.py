import random
import turtle as turtle


turtle.setup(width=600, height=600, startx=0, starty=0)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big
def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """

    print('turtle clicked!')
    
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    t.goto(x, y)
    set_turtle_image(t, 'pikachu.gif')

# Connect the turtle to the turtle_clicked function
while True:
    t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))


turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
