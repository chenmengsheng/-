A={}
Letter='abcdehghijklmnopqrstuvwxyz'
for char in 'abcdehghijklmnopqrstuvwxyz':
    A[char]=0
print(A)
while True:
    try:
        s=input().lower()
        for char in s:
            if char in Letter:
                A[char]+=1
    except:
        break
print(A)