class Fraction:
    def __init__(self, _up, _down):
        self.up = _up
        self.down = _down

    def show(self):
        print("%d/%d" % (self.up, self.down))

def Print(f):
    print("%d/%d" % (f.up, f.down))


a = Fraction(1, 2)  # a=1/2
#Print(a)#Ugly bad smell
a.show()
print(a)#ugly
b = Fraction(3,9)
b.show()
