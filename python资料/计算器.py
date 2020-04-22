# coding: utf-8
# 将tkinter改为Tkinter兼容Python 2.x
from tkinter import *
class App:
 def __init__(self, master):
  self.master = master
  self.initWidgets()
  self.hi = None
 def initWidgets(self):
  # 创建一个输入组件
  self.show = Label(relief=SUNKEN, font=('Courier New', 24),\
   width=23, bg='white', anchor=W)
  # 对该输入组件使用Pack布局，放在容器顶部
  self.show.pack(side=TOP, pady=10)
  p = Frame(self.master)
  p.pack(side=TOP)
  # 定义字符串的元组
  names = ("+", "1" , "2" , "3" , "↺"
   ,"-", "4" , "5" , "6" , "**" , "*", "7" , "8"
   , "9", "//", "/" , "." , "0" , "%", "=")
  # 遍历字符串元组
  for i in range(len(names)):
   # 创建Button，将Button放入p组件中
   b = Button(p, text=names[i], font=('Verdana', 20), width=5)
   b.grid(row=i // 5, column=i % 5)
   # 为鼠标左键的单击事件绑定事件处理方法
   b.bind('<Button-1>', self.click)
   # 为鼠标左键的双击事件绑定事件处理方法
   if b['text'] == '↺': b.bind('<Button-1>', self.clean)
  # 定义一个记录输入数字次数的变量
  self.i = 0
 def click(self, event):
  # 如果用户单击的是数字键或点号
  if(event.widget['text'] in ('0', '1', '2', '3',\
   '4', '5', '6', '7', '8', '9', '.')):
   # 判断self.i是否为0，0的话清空show['text']的值
   if self.i == 0 :
    self.show['text'] = ''
   self.show['text'] = self.show['text'] + event.widget['text']
   self.i = self.i + 1
   print(self.i)
  # 如果用户单击了运算符
  elif(event.widget['text'] in ('+', '-', '*', '/', '%', '**', '//')):
   # 把输入的数字与输入的字符相结合，组成一个数学运算式
   self.show['text'] = self.show['text'] + event.widget['text']
  elif(event.widget['text'] == '=' and self.show['text'] is not None):
   # 赋值给self.hi
   self.hi = self.show['text']
   # 其实这一步可以不要，主要作用是在调试时可以在后台看输入的数据
   print(self.hi)
   # 使用eval函数计算表达式的值
   self.show['text'] = str(eval(self.hi))
   self.hi = None
   self.i = 0
 # 点击↺（恢复）按钮时，程序清空计算结果、将表达式设为None
 def clean(self, event):
  self.hi = None
  self.show['text'] = ''
root = Tk()
root.title("简单科学计算器")
App(root)
root.mainloop()
