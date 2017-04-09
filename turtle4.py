# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 08:41:17 2017

@author: loulan
"""
"""
#draw a picture
import turtle
import time
t = turtle.Turtle()
t.speed(0)
move =1
for i in range(180):
    t.color("green")
    t.right(move)
    t.penup()
    t.fd(100)
    t.pendown()
    t.left(36)
    t.fd(120)
    t.left(36)
    t.circle(20)
    t.home()
    move+=2
t.done()
"""

"""
#draw a picture likely a sunflowers
import turtle
import time
t = turtle.Turtle()
t.shape("turtle")
t.color("red","yellow")
t.begin_fill()
while True:
    t.fd(200)
    t.left(170)
    if abs(t.pos())<1:
        break
t.end_fill()
time.sleep(15)
"""






































    