f = open("data.in", "r");
crabPositions = [ int(p) for p in f.readline().split(',') ]
minFuel = float("inf")
for p in range(max(crabPositions)):
    f = 0
    for k in crabPositions:
        f += (abs(p-k)/2)*(abs(p-k)+1)
    if minFuel>f:
        minFuel = int(f)
print(minFuel)
