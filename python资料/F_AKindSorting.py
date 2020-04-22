class Rectangle:
    def __init__(self, _number, _length, _width):
        self.number, self.length, self.width = _number, _length, _width

    def __repr__(self):  # __repr__
        return '%d %d %d' % (self.number, self.length, self.width)

    def __lt__(self, other):
        if self.number != other.number:
            return self.number < other.number
        if self.length < other.length:
            return self.length < other.length
        return self.width < other.width


T = int(input())
for t in range(T):
    n = int(input())
    rectangles = []
    for i in range(n):
        number, length, width = map(int, input().strip().split())
        if length < width:
            length, width = width, length
        rectangles.append(Rectangle(number, length, width))
    rectangles.sort()
    # print(rectangles)
    print(rectangles[0])
    for j in range(1, len(rectangles)):
        if rectangles[j - 1] < rectangles[j]:
            print(rectangles[j])
