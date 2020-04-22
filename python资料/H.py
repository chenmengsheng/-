class Time:
    def __init__(self, _hour, _minute, _second):
        self.hour = _hour
        self.minute = _minute
        self.second = _second

    def __str__(self):
        return '%02d:%02d:%02d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        ans = Time(0, 0, 0)
        ans.second = self.second + other.second
        carry = ans.second // 60
        ans.second %= 60
        ans.minute = self.minute + other.minute + carry
        carry = ans.minute // 60
        ans.minute %= 60
        ans.hour = (self.hour + other.hour + carry) % 24
        return ans


import sys

lines = sys.stdin.readlines()

for line in lines:
    h1, m1, s1, h2, m2, s2 = map(int, line.strip().split())
    a = Time(h1, m1, s1)
    b = Time(h2, m2, s2)
    print(a + b)
