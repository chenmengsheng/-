# -*- coding:utf-8 –*-
# 用递归函数实现turtle画一棵树。
# 所有递归函数都可以转化为非递归来实现，
# 如果需要非递归方法的代码，请加公众号：see_goal 留言“turtle画树”
import turtle

p = turtle.Pen()
p.penup()
p.goto(0, -200)
p.setheading(90)
p.pensize(7)
p.pencolor('green')
p.pendown()


def branch(plist, len):  # 自定义函数，画树枝
    if (len > 15):  # 递归的退出条件
        list = []  # 新画笔列表
        for p in plist:  # 遍历旧画笔列表
            p.forward(len)
            q = p.clone()
            p.left(65)
            q.right(65)
            list.append(p)  # 存入新画笔列表
            list.append(q)  # 存入新画笔列表
        branch(list, len * 0.65)  # 递归，list为新画笔列表，树枝长65%


branch([p], 200)
turtle.done()
