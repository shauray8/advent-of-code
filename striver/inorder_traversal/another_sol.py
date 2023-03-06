class tree:
    def __init__(self, val, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left

class stack:
    def __init__(self, size=1000, top=-1):
        self.size = size
        self.top = top
        self.arr = [0]*size

    def push(self,x):
        self.top += 1
        self.arr[self.top] = x

    def Top(self):
        return self.arr[self.top]

    def pop(self):
        x = self.arr[self.top]
        self.top -= 1
        return x

    def empty(self):
        if self.top == -1:
            return True
        return False

a = tree(1)
b = tree(2)
c = tree(3)
d = tree(4)
e = tree(5)

a.left = b
a.right = c
b.left = c
c.left = d
c.right = e

valval = []
def inorder(tree):
    if not tree: return
    inorder(tree.left)
    valval.append(tree.val)
    inorder(tree.right)

s = stack()
def it_inorder(tree):
    while True:
        if tree:
            s.push(tree)
            tree = tree.left
        else:
            if s.empty(): return
            tree = s.Top()
            valval.append(tree.val)
            s.pop()
            tree = tree.right

it_inorder(a)
print(valval)

