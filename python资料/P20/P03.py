# 3.    打印数字图形：
def printTriangle(n):
    for i in range(n + 1):
        print("  " * (n - i), end=' ')
        for j in range(i + 1):
            print(j + 1, end=' ')
        for j in range(i):
            print(i - j, end=' ')
        print()
    for i in range(n):
        print("  " * (i + 1), end=' ')
        for j in range(n - i):
            print(j + 1, end=' ')
        for j in range(n - i - 1):
            print(n - i - j - 1, end=' ')
        print()


printTriangle(4)
