import math


# ver1.0

class Fraction:
    def __init__(self, _up=0, _down=1):  # 构造方法 Constructor
        self.up, self.down = _up, _down
        self.simplify()

    def __str__(self):  # 字符串化
        return "%d/%d" % (self.up, self.down)

    def simplify(self):
        g = math.gcd(self.up, self.down)
        self.up, self.down = self.up // g, self.down // g

    def add(self, other):
        c = Fraction(0, 1)
        c.down = self.down * other.down
        c.up = self.up * other.down + self.down * other.up
        c.simplify()
        return c


print(Fraction())#0/1
print(Fraction(3))#3/1
print(Fraction(3,9))#1/3

#1/1+1/2+...+1/10
s = Fraction()
for i in range(1, 101):
    s =s.add(Fraction(1,i))
print(s)
