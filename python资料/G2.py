class Person:  # PERSON
    def __init__(self, _name, _y, _m, _d):
        self.name = _name
        self.y = _y
        self.m = _m
        self.d = _d

    def __repr__(self):
        return '%s %04d-%02d-%02d' % (self.name, self.y, self.m, self.d)

    def __lt__(self, other):
        if self.y != other.y: return self.y < other.y
        if self.m != other.m: return self.m < other.m
        if self.d != other.d: return self.d < other.d
        return self.name < other.name


import sys

lines = sys.stdin.readlines()[1:]

for line in lines:
    print(line)
