'''
18.	某本书的页码从1开始，小明算了算，总共出现了202个数1，试编程求这本书一共有多少页？
'''


def ones(n):
    if n < 10:
        return n % 10 == 1
    return ones(n // 10) + ones(n % 10)


print(ones(1231))  # uni-testing

tot = 0
for p in range(1, 100000):
    tot += ones(p)
    if tot >= 202:
        break
if tot == 202:
    print(p)
else:
    print('Impossible')
