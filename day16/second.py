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

finalticket =[]
error = 0
aa=0
for i in range(len(ticket)):
    for j in range(len(ticket[i])):
        #print(ticket[i][j])
        aa +=int(ticket[i][j])
        for k in range(20):

            if (int(ticket[i][j]) in range(int(finalrange[k][0]),int(finalrange[k][1]))):
                finalticket.append(ticket[i])
                #print(finalrange[k][0], finalrange[k][1])
                error += int(ticket[i][j])
                break
            break
        break
    

# print(len(finalticket))

print(len(ticket))

def calc(ll):
    e = []
    for j in range(len(finalticket[0])):
        a = 0

        for i in finalticket:
            #for j in range(len(i)):
            #print(i[0])
            if (int(i[j]) in range(int(finalrange[ll][0]),int(finalrange[ll][1])+1)) or (int(i[j]) in range(int(finalrange[ll+1][0]),int(finalrange[ll+1][1])+1)):
                a+=1

        e.append(a)
    print(e)
    # for i in range(len(e)):
    #     if int(e[i]) == len(finalticket):
    #         print(i)


for i in range(0,len(finalrange),2):
    calc(i)
    print("   ")

    
