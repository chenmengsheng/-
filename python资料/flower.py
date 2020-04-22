import math
while True:
    n=int(input())
    if n==0:break
    c=n%10
    b=(n//10)%10
    a=n//10
    if a**3+b**3+c**3=n:
        print('Yes')
    else:
        print('No')
