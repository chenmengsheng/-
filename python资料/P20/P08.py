'''
8.    选人。一个小组共五人，分别为A、B、C、D、E。现有一项任务，要他们中的3个人去完成。
已知：
（1）A、C不能都去；
（2）B、C不能都不去；
（3）如果C去了，D、E就只能去一个，且必须去一个；
（4）B、C、D不能都去；
（5）如果B去了，D、E就不能都去。编程找出此项任务该由哪三人去完成的所有组合。
'''
a, b, c, d, e = 0, 0, 0, 0, 0
for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            for d in range(0, 2):
                for e in range(0, 2):
                    if a == 1 and c == 1: continue
                    if b == 0 and c == 0: continue
                    if c == 1 and d + e != 1: continue
                    if b == 1 and c == 1 and d == 1: continue
                    if b == 1 and d == 1 and d == 1: continue
                    if a + b + c + d + e == 3:
                        print(a, b, c, d, e)
