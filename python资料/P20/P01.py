# coding=utf-8
# 1.	随机产生一些1—100之间的整数，直到产生的数为50为止。
import random

while True:
    n = random.randint(1, 100)
    print(n, end=' ')
    if n == 50:
        break
print()
