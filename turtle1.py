# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 11:55:07 2017

@author: loulan
"""
"""
#一边实例敲代码，一边看turtle官方文档
#google example the first example
import turtle 
import time
t = turtle.Pen()
wn= turtle.Screen()
wn.bgcolor('black')

colors = ['red','purple','blue','green','yellow','orange']
t.speed(0)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)
    
time.sleep(10)
"""
"""
#the second example
from turtle import *
color('red','yellow')
begin_fill()
while True:
    forward(200)
    left(175)
    if abs(pos())<1:
        break
end_fill()
done()
"""
"""
#the third example
import turtle
import time
t = turtle.Turtle()
for x in range(1,11):
    t.speed(5)    
    t.right(40)
    t.pencolor("blue")
    t.circle(50)
    t.right(30)
    t.pencolor("green")
    t.circle(100)
    t.circle(70)
    t.circle(50)
    t.pencolor("red")
    t.circle(80)
    t.circle(90)
    t.left(10)
    t.pencolor("yellow")
    t.right(5)
time.sleep(5)
"""
"""
#the fourth example
import turtle
import time
t  = turtle.Turtle()
def draw_pic(length,sides):
    for x in range(sides):
        t.fd(length)
        t.lt(360/sides)
print("let's draw a picture")
how_long= int(input("would you like how long is it?"))
how_angle= int(input("would you like how long is it?"))
draw_pic(how_long,how_angle)
time.sleep(5)
"""
"""
#the 5th example
import turtle
t =turtle.Turtle()
move = 1
t.speed(0)
for i in range(180):
    t.pendown()
    t.right(move)
    t.forward(40)
    t.left(40)
    t.forward(12)
    t.circle(20)
    t.right(30)
    t.forward(60)
    t.left(30)
    t.fd(30)
    t.right(20)
    t.fd(26)
    t.circle(10)
    t.left(13)
    t.fd(35)
    t.right(45)
    t.circle(25)
    t.bk(10)
    t.right(20)
    t.fd(26)
    t.circle(10)
    t.left(13)
    t.fd(35)
    t.right(45)
    t.circle(25)
    t.bk(10)
    
    t.penup()
    t.home()
    move+=2
"""
"""
#the 6th example
import turtle
turtle.speed(0)
def c_curse(turtle,x1,y1,x2,y2,level):
    def drawLine(x1,y1,x2,y2):
        turtle.up()
        turtle.goto(x1,y1)
        turtle.down()
        turtle.goto(x2,y2)
    if level == 0:
        drawLine(x1,y1,x2,y2)
    else:
        xm = (x1+x2+y1-y2)/2
        ym = (x2+y1+y2-x1)/2
        c_curse(turtle,x1,y1,xm,ym,level-1)
        c_curse(turtle,xm,ym,x2,y2,level-1)
def main():
    #turtle = Turtle(300,350)
    #turtle.setWidth(1)
    c_curse(turtle,75,-75,75,75,14)
main()
"""


             
































