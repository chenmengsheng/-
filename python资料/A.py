class Pipe:
    def __init__(self, _length, _diameter, _number):
        self.length, self.diameter, self.number = _length, _diameter, _number

    def __str__(self):
        return str(self.number)

    def __lt__(self, other):
        if self.length != other.length:  # 第一关键字 descending
            return self.length > other.length
        if self.diameter != other.diameter:  # 第二关键字 ascending
            return self.diameter < other.diameter
        return self.number > other.number


T = int(input())
for i in range(T):
    n = int(input())
    pipes = []
    for j in range(n):
        length, diameter, number = map(int, input().strip().split())
        pipes.append(Pipe(length, diameter, number))
    pipes.sort()
    print(pipes[0].number)
