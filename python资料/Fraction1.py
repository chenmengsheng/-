class Fraction:
    def __init__(self, _up, _down):
        self.up = _up
        self.down = _down

    def show(self):
        print("%d/%d" % (self.up, self.down))
    def getInfo(self):
        return "%d/%d" % (self.up, self.down)
    def __str__(self):
        return "%d/%d" % (self.up, self.down)

a = Fraction(1, 2)  # a=1/2
a.show()
print(a.getInfo())#ugly
print(a)#neat