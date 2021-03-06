from turtle import *
from random import *
from math import *


def tree(n, l):
    pd() #下笔
    # 阴影效果
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t, t, t,)
    pensize(n/4)
    forward(l)  # 画树枝
    if n > 0:
        b = random()*15+10  # 右分支偏转角度
        c = random()*15+10  # 左分支偏转角度
        d = l*(random()*0.35+0.6)  # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n-1, d)
        # 左转一定角度，画右分支
        left(b+c)
        tree(n-1, d)
        right(c)  # 转回来
    else:
        right(90)  # 画叶子
        n = cos(radians(heading()-45))/4+0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)


bgcolor(0.5, 0.5, 0.5)  # 背景色
ht()  # 隐藏turtle
speed(0)    # 速度0-10渐进，0最快
tracer(0, 0)
left(90)
pu()    # 抬笔
backward(300)   # 后退300
tree(13, 100)   # 递归
done()
