import math

#ver1.0

class Fraction:
    def __init__(self, _up, _down):  # 构造方法 Constructor
        self.up, self.down = _up, _down
        self.simplify()

    def __str__(self):#字符串化
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


a = Fraction(3, 9)  # 创建一个对象  实例化 instantiate
b = Fraction(4, 24)
c = a.add(b)
# c = a + b
print(c)
