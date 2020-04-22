# 2计算1—1000之间能同时被3和5整除的整数的和。
def r_sum(start, end, mod):
    start, end = (start + mod - 1) // mod * mod, end // mod * mod
    return (start + end) * ((end - start) / mod + 1) / 2


print(int(r_sum(1, 1000, 15)))
