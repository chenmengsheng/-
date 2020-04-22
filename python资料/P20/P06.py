'''
赵、钱、孙、李、周五人围着一张圆桌吃饭。饭后，周回忆说：“吃饭时，赵坐在钱旁边，钱的左边是孙或李”；李回忆说：“钱坐在孙左边，我挨着孙坐”。
结果他们一句也没有说对。请问，他们在怎样坐的？
'''


def left(a, b):
    return a + 1 == b or a == 5 and b == 1


def right(a, b):
    return left(b, a)


def adj(a, b):
    return right(a, b) or left(a, b)


zhao, qian, sun, li, zhou = 1, 1, 1, 1, 1
for qian in range(2, 6):
    for sun in range(2, 6):
        if sun == qian: continue
        for li in range(2, 6):
            if li == qian or li == sun:
                continue
            zhou = 15 - zhao - qian - sun - li
            if adj(zhao, qian) or left(qian, sun) or left(qian, li):
                continue
            if left(sun, qian) or adj(sun, li):
                continue
            print("%d %d %d %d %d" % (zhao, qian, sun, li, zhou))
