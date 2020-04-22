class Rectangle:
    def __init__(self, _number, _length, _width):
        self.number, self.length, self.width = _number, _length, _width

    def __repr__(self):  # __repr__
        return '%d %d %d' % (self.number, self.length, self.width)

    def __lt__(self, other):  # <
        if self.number != other.number:
            return self.number < other.number
        if self.length < other.length:
            return self.length < other.length
        return self.width < other.width

    def __eq__(self, other):  # ==
        return self.__hash__()==other.__hash__()

    def __hash__(self):
        return number * 100000 * 100000 + length * 100000 + width


T = int(input())
for t in range(T):
    n = int(input())
    rectangles = set()
    for i in range(n):
        number, length, width = map(int, input().strip().split())
        if length < width:
            length, width = width, length
        rectangles.add(Rectangle(number, length, width))
    L=list(rectangles)
    L.sort()
    print(L)
