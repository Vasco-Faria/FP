# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

t = turtle.Turtle()

# Use t.up(), t.down() and t.goto(x, y)

# Put your code here

fil=open("drawing.txt")

for line in fil:
    a=line.strip()
    if "UP" in a:
        t.up()
    elif "DOWN" in a:
        t.down()
    else:
        c=a.split(" ")
        t.goto(float(c[0]),float(c[1]))





# wait
turtle.Screen().exitonclick()

