# 学习了海龟绘图，总结一下//直接看官方文档，一定要直接看官方文档

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

