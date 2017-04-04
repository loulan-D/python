# 学习了海龟绘图，总结一下//直接看官方文档，一定要直接看官方文档
#昨天学习了海龟绘图，google了大量的教程，一个网页一个网页的看，最后差不多都看了，但是在实践的过程中发现有好多错误，因为看的一部分教程是2.7版本的，
#python3的好多已经淘汰了，虽说看这些内容确实有效，但效率却非常的低，不如直接看官方教程，直接看python库，权威！
#不要惧怕英语！
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

