import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(7)

def h1():
    tess.forward(100)
    tess.left(56)

wn.ontimer(h1, 3000)
wn.mainloop()