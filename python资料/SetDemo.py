a = [1, 1, 3, 6, 6, 6, 7]
a.sort()
print(a[0])
for j in range(1, len(a)):
    if a[j - 1] < a[j]:
        print(a[j])

S = set()
for i in a: S.add(i)
print(S)
