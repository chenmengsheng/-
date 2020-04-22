'''
16.	试编程找出能被各位数字之和整除的一切两位数。
'''
for n in range(10, 99 + 1):
    a, b = n // 10, n % 10
    if n % (a + b) != 0: continue
    print(n, end=' ');
print()
