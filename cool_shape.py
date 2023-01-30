from turtle import *

bgcolor('black')
speed(-100)
hideturtle()
for i in range(120):
    color('red')
    circle(i)
    color('orange')
    circle(1*.08)
    right(3)
    forward(3)
done()