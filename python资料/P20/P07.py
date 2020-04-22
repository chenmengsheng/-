'''
7. 找数。一个三位数，各位数字互不相同，十位数字比个位、百位数字之和还要大，且十位、百位数字之和不是质数。编程找出所有符合条件的三位数。
注：1.   不能手算后直接打印结果。
'''
import math


def prime(n):
    for c in range(2, int(math.sqrt(n))):
        if n % c == 0:
            return False
    return True


for n in range(100, 1000):
    a, b, c = n // 100, (n % 100) // 10, n % 10
    if a == b or b == c or c == a or b <= a + c or prime(b + c):
        continue
    print(n, end=" ")
