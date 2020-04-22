class Point:
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def __repr__(self):
        return '(%d,%d)' % (self.x, self.y)


import random,math

points = []
for i in range(10):
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    points.append(Point(x, y))
print(points)
print(sorted(points, key=lambda p: p.x))  # ascending by x
print(sorted(points, key=lambda p: -p.x))  # descending by x
print(sorted(points, key=lambda p: p.x * 100 + p.y))  # ascending by x ,y
print(sorted(points, key=lambda p: (p.x, p.y)))  # ascending by x ,y
me = Point(5, 5)
print(sorted(points, key=lambda p: (math.sqrt((p.x-me.x)**2+(p.y-me.y)**2))))  # wechat
