def Max(a=0, b=0, c=0):
    t = a
    if b > t: t = b
    if c > t: t = c
    return t


print(Max())#Max(0,0,0)
print(Max(1))#Max(1,0,0)
print(Max(2, 3))#Max(2,3,0)
print(Max(3, 4, 5))#
