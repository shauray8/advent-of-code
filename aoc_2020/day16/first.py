lis = []
w = open('range.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)
finalrange = []

for i in range(len(lis)):

    a,b = lis[i].split(" ")[-1], lis[i].split(' ')[-3]
    finalrange.append(a.split("-"))
    finalrange.append(b.split("-"))


#print(rangecheck)

nearby = []
w = open('nearby.txt','r')
nearby.append(w.read())
nearby = nearby[0].split("\n")
nearby.pop(-1)
ticket = []
for i in range(len(nearby)):
    ticket.append(nearby[i].split(","))


#print(finalrange)

error = 0
aa=0
for i in range(len(ticket)):
    for j in range(len(ticket[i])):
        #print(ticket[i][j])
        aa +=int(ticket[i][j])
        for k in range(20):
            
            if (int(ticket[i][j]) in range(int(finalrange[k][0]),int(finalrange[k][1]))):
                #print(ticket[i][j])
                #print(finalrange[k][0], finalrange[k][1])
                error += int(ticket[i][j])
                break
        

print("error: ",aa-error)
