lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)
print(lis)

#if a cube is active and 2 or 3 of its neigbors are also active == cube remains active
#if a cube is inactive 3 of its neigbors are active == cube becomes active 

ON= set()

for r,l in enumerate(lis):
    for c,ch in enumerate(l):
        if ch == "#":
            ON.add((r,c,0))
            

for _ in range(6):
    NEW_ON = set()
    for x in range(-15,15):
        for y in range(-15,15):
            for z in range(-15,15):
                nbr = 0
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        for dz in [-1,0,1]:
                            if dx!=0 or dy!=0 or dz!=0:
                                if (x+dx, y+dy, z+dz) in ON:
                                    nbr += 1
                if (x,y,z) not in ON and nbr == 3:
                    NEW_ON.add((x,y,z))
                if (x,y,z) in ON and nbr in [2,3]:
                    NEW_ON.add((x,y,z))
    ON = NEW_ON
    
print(len(ON)) 

