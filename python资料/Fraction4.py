import math


# ver1.0

class Fraction:
    def __init__(self, _up, _down):  # 构造方法 Constructor
        self.up, self.down = _up, _down
        self.simplify()

    def __repr__(self):  # 字符串化2
        return "%d/%d" % (self.up, self.down)

    def simplify(self):
        g = math.gcd(self.up, self.down)
        self.up, self.down = self.up // g, self.down // g

    def __add__(self, other):
        c = Fraction(0, 1)
        c.down = self.down * other.down
        c.up = self.up * other.down + self.down * other.up
        c.simplify()
        return c

    def __lt__(self, other):  # < less than
        return self.up * other.down < other.up * self.down


a = Fraction(3, 9)
b = Fraction(4, 24)
c = a + b

print(b < a)
A = [a, b, c]
A.sort()
for f in A:
    print(f)
print(A)