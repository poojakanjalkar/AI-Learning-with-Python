import turtle

screen = turtle.Screen()
screen.title("Draw a Triangle")


triangle = turtle.Turtle()


triangle.speed(3)
triangle.pensize(3)

# Draw a triangle
for _ in range(3):
    triangle.forward(100)  
    triangle.left(120)     


turtle.done()
