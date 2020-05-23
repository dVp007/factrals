#snowFlakes
import turtle
import random

wn = turtle.Screen()
wn.bgcolor('cyan')

elsa = turtle.Turtle()
elsa.speed(15)

sfcolors = ["white", "blue", "purple", "grey", "magenta"]

def snowFlakes(size):
    elsa.penup()
    elsa.forward(10*size)
    elsa.left(45)
    elsa.pendown()
    elsa.color(random.choice(sfcolors))
    for i in range(8):
        branch(size)
        elsa.left(45)

def branch(size):
    for i in range(3):
        for i in range(3):
            elsa.forward(10.0*size/3)
            elsa.backward(10.0*size/3)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(10.0*size/3)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(10.0*size/3)

for i in range(20): 
    x = random.randint(-200, 200) 
    y = random.randint(-200, 200) 
    sf_size = random.randint(1, 4) 
    elsa.penup() 
    elsa.goto(x, y) 
    elsa.pendown() 
    snowFlakes(sf_size)
wn.exitonclick()