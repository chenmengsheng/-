import math


class Fraction:
    def __init__(self, _up, _down):  # 构造方法 Constructor
        g = math.gcd(_up, _down)
        self.up = _up // g
        self.down = _down // g

    def __str__(self):
        return "%d/%d" % (self.up, self.down)

    def add(self, other):#bad smell
        c = Fraction(0, 1)
        c.down = self.down * other.down
        c.up = self.up * other.down + self.down * other.up
        return c


a = Fraction(3, 9)  # 创建一个对象  实例化 instantiate
print(a)  # neat
b = Fraction(4, 24);
c = a.add(b)
# c = a + b
print(c)
