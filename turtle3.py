# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 12:03:01 2017

@author: loulan
"""

import turtle 
t = turtle.Turtle()
t.speed(0)
t.home()
t.forward(166)
t.color("red")
for i in range(180):
    t.circle(55)
    t.forward(55)
    t.left(55)
    t.fd(100)
t.penup()
t.home()
t.forward(360)
t.color("green")
t.write("Hello world!")

    
t.done()