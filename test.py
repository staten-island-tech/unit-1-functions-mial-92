import turtle
from turtle import *
t = Turtle()
t.shape('turtle')
turtle.done
def message(x):
    print('hello')

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
t.forward(120)
def equal(a):
    t.forward(a)
    t.left(120)
    t.forward(a)
    t.left(120)
    t.forward(a)
equal(90)