class stack:
    def __init__(self, size=1000, top=-1):
        self.size = size
        self.top = top
        self.arr = [0]*size)

    def push(self,x):
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        x = self.arr[self.top]
        self.top -= 1
        return x

    def Top(self):
        return self.arr[self.top]

    def Size(self):
        return self.top+1

s = stack()
s.push(7)
s.push(8)
s.push(9)
s.push(10)

print(s.Size())




