a = [1, 3, 3, 6, 1, 5, 7]
# a.sort()
# for i in a:print(i,end=" ")
# print('')
# print ascending
for i in sorted(a):
    print(i, end=" ")
print('')
# print descending
for i in sorted(a)[::-1]:
    print(i, end=" ")
print('')

# print with lambda
for i in sorted(a, key=lambda x: x):
    print(i)
