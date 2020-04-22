class Leader:
    def __init__(self, _name, _count=0):
        self.name = _name
        self.count = _count

    def __str__(self):
        return '%s:%d' % (self.name, self.count)


leader = [Leader("Li"), Leader("Zhang"), Leader("Fun")]
# Ctrl+Alt+L
n = int(input().strip())
for i in range(n):
    name = input().strip()
    if name == 'Li':
        leader[0].count += 1
    if name == 'Zhang':
        leader[1].count += 1
    if name == 'Fun':
        leader[2].count += 1

for each in leader:
    print(each)
