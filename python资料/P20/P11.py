'''
11.    甲、乙、丙、丁四人共有糖若干块，
甲先拿出一些糖分给另外三人，使他们三人的糖数加倍；
乙拿出一些糖分给另外三人，也使他们三人的糖数加倍；
丙、丁也照此办理，此时甲、乙、丙、丁四人各有16块，
编程求出四个人开始各有糖多少块。
'''


def solve(n):
    a, b, c, d = 0, 0, 0, 0
    for a in range(n // 2, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                d = n - a - b - c
                ca, cb, cc, cd = a, b, c, d
                ca, cb, cc, cd = ca - cb - cc - cd, 2 * cb, 2 * cc, 2 * cd
                cb, cc, cd, ca = cb - cc - cd - ca, 2 * cc, 2 * cd, 2 * ca
                cc, cd, ca, cb = cc - cd - ca - cb, 2 * cd, 2 * ca, 2 * cb
                cd, ca, cb, cc = cd - ca - cb - cc, 2 * ca, 2 * cb, 2 * cc
                if ca == n / 4 and cb == n / 4 and cc == n / 4 and cd == n / 4:
                    print(a, b, c, d)
                    # 以下验证一下
                    ca, cb, cc, cd = a, b, c, d
                    ca, cb, cc, cd = ca - cb - cc - cd, 2 * cb, 2 * cc, 2 * cd
                    print(ca, cb, cc, cd)
                    cb, cc, cd, ca = cb - cc - cd - ca, 2 * cc, 2 * cd, 2 * ca
                    print(ca, cb, cc, cd)
                    cc, cd, ca, cb = cc - cd - ca - cb, 2 * cd, 2 * ca, 2 * cb
                    print(ca, cb, cc, cd)
                    cd, ca, cb, cc = cd - ca - cb - cc, 2 * ca, 2 * cb, 2 * cc
                    print(ca, cb, cc, cd)


solve(64)
