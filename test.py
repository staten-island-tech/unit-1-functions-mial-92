import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
turtle.done
def message(x):
    print('hello')


""" def equal(a):
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.left(120)
    t.forward(a)
equal(90)  """
""" 
def square(x,y):
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.left(90)
square(125,100)

size = 35 
for i in range(60):
    square(size, size)
    t.left(5)
    size += 5

    t.speed(0)
 """
def spiralstar(x):
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144) 
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
spiralstar(144)

size = 35
for i in range(60):
    spiralstar(size)
    t.left(5)
    size += 5
    
    t.speed(0)