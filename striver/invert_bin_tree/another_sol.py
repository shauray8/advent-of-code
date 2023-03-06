class tree:
    def __init__(self, val, right=None, left=None):
        self.right = right
        self.left = left
        self.val = val

a = tree(19)
b = tree(20)
c = tree(21)
d = tree(22)
e = tree(23)

a.right = b
a.left = c
a.right.right = d
a.right.right = e

def invert(tree):
    if tree:
        left = tree.left
        right = tree.right
        tree.right = left
        tree.left = right
        invert(tree.left)
        invert(tree.right)
    return tree

tree = invert(a)
print(tree.left.left.val)

