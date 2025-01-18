import turtle

def draw_arc(t, radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius, 180)  
    t.end_fill()

def draw_rainbow():
    screen = turtle.Screen()
    screen.bgcolor("skyblue") 

   
    t = turtle.Turtle()
    t.speed(0)
    t.penup()

   
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    radius = 200 

   
    for color in colors:
        t.goto(0, -radius) 
        t.pendown()
        draw_arc(t, radius, color)
        t.penup()
        radius -= 20 

   
    t.hideturtle()

  
    screen.mainloop()


draw_rainbow()
