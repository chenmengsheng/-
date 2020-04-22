class Rectangle:
    def __init__(self, _number, _length, _width):
        self.number = _number
        self.length = _length
        self.width = _width

    def __repr__(self):
        return '%d %d %d' % (self.number, self.length, self.width)

    def __eq__(self, other):
        return self.number == other.number and self.width == other.width and self.length == other.length

    def __lt__(self, other):
        if self.number != other.number: return self.number < other.number
        if self.width != other.width: return self.width < other.width
        return self.length < other.length

    def __hash__(self):
        return self.number * 10000 * 10000 + self.width * 10000 + self.length


