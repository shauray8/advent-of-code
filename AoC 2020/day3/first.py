lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)

li =[ 
"..##.......",
"#...#...#..",
".#....#..#.",
"..#.#...#.#",
".#...##..#.",
"..#.##.....",
".#.#.#....#",
".#........#",
"#.##...#...",
"#...##....#",
".#..#...#.#"] 

a, b, tree = 0,0,0

for i in range(len(lis)):
    lis[i] = lis[i]*100

#print(len(lis))

for i in range(1,len(lis)):
    a += 1
    b += 3
    print(lis[a][b])
    if lis[a][b] == '#':
        tree += 1

print(f"number of trees: {tree}")

# First try baby !!
