
# coding: utf-8
import random
import sys
# 定义棋盘的大小
BOARD_SIZE = int(input('请输入棋盘大小:'))
#BOARD_SIZE = int(BOARD_SIZE)
high = []
wide = []
num = []
num1 = []
num2 = []
# 定义一个二维列表来充当棋盘
board = []
def initBoard() :
    # 把每个元素赋为"╋"，用于在控制台画出棋盘
    for i in range(BOARD_SIZE) :
        row = ["╋"] * BOARD_SIZE
        board.append(row)
# 在控制台输出棋盘的方法
def printBoard() :
    # 打印每个列表元素
    for i in range(BOARD_SIZE) :
        for j in range(BOARD_SIZE) :
            # 打印列表元素后不换行
            print(board[i][j], end="")
        # 每打印完一行列表元素后输出一个换行符
        print()
initBoard()
printBoard()
# 随机生成2位数字,并判断是否和手动输入相同（相同的话重新获取）
def randoms():
    a,b = [random.randint(1, BOARD_SIZE) for j in range(1, 3)]
    for i in range(len(wide)) :
       if wide[i] == a and high[i] == b :
          randoms()
       else:
          board[a - 1][b - 1]= "○"
# 判断五位数字是否相连
def sorts(num) :
   num.sort()
   n = 0
   j = 0
   n = num[0]
   for i in num :
      if i == n :
         n = i + 1
         j=j+1
         if j >= 5:
             printBoard()
             print('成功')
             sys.exit()
      else:
         n = i
         n = n + 1
         j = 1
while 1 > 0 :
    inputStr = input("请输入您下棋的坐标，应以x,y的格式：\n")
    if inputStr != None :
        # 将用户输入的字符串以逗号（,）作为分隔符，分隔成2个字符串
        x_str, y_str = inputStr.split(sep = ",")
        # 把对应的列表元素赋为"●"。
        board[int(y_str) - 1][int(x_str) - 1] = "●"
        # 记录输入的x_str和y_str
        wide.append(int(x_str))
        high.append(int(y_str))
        # 进行是否成功判断
        if len(wide) >= 5 :
           for i in range(len(wide)) :
              if (wide[i]+int(y_str))/(high[i]+int(x_str)) == 1 :
                 num.append(wide[i])
                 sorts(num)
              if wide[i] == int(x_str):
                 num1.append(high[i])
                 sorts(num1)
              if high[i] == int(y_str):
                 num2.append(wide[i])
                 sorts(num2)
           num.clear()
           num1.clear()
           num2.clear()
        randoms()
        printBoard()
    else :
        print('输入格式不对') 
        break

