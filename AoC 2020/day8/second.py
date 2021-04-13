lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)
acc = 0
bb = True
i = 0
check = []
while(bb):
    print(i,lis[i])
    if lis[i][:3] == "acc":
        #print(lis[i].split(" ")[1])
        acc += int(lis[i].split(" ")[1])
        check.append(i)
    elif lis[i][:3] == 'jmp':
        i = i + eval(lis[i].split(" ")[1])-1
        #print("good",i)
    i += 1
    if i in check:
        bb = False
print(acc)
