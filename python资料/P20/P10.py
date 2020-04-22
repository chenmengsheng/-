# 10.A、B、C三人进入决赛，赛前A说：“B和C得第二，我得第一”；B说：“我进入前两名，C得第三名”；C说：“A不是第二，B不是第一”。比赛产生了一、二、三名，比赛结果显示：获得第一的选手全说对了，获得第二的选手说对了一句，获得第三的选手全说错了。编程求出A、B、C三名选手的名次。
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            if a == b or b == c or c == a:
                continue
            pa, pb, pc = 0, 0, 0
            if b == 2 and c == 2:
                pa += 1
            if a == 1:
                pa += 1
            if b <= 2:
                pb += 1
            if c == 3:
                pb += 1
            if a != 2:
                pc += 1
            if b != 1:
                pc += 1
            if a + pa == b + pb and b + pb == c + pc:
                print(a, b, c)
