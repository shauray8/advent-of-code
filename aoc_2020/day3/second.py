lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)


for i in range(len(lis)):
    lis[i] = lis[i]*100

#print(len(lis))

def count_tree(right,down):
    a, b, tree = 0,0,0
    for i in range(1,len(lis)):
        a += down
        b += right
        #print(lis[a][b])
        # try except block because of the range issues in [1,2] 
        try:
            if lis[a][b] == '#':
                tree += 1
        except Exception as e:
            pass
    return tree

final = 1
for i in range(5):
    calc = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    trees = count_tree(calc[i][0],calc[i][1])
    final *= trees
    print(trees)

print(f"final answer: {final}")


