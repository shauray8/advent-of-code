lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n\n")

ON = []
for i in lis:
    ON.append(i)

for i in ON:
    break

CHECK = ['byr',
'iyr',
'eyr',
'hgt',
'hcl',
'ecl',
'pid',
'cid']
FINAL = []
for i in ON:
    NEW = []
    #print(i.strip())
    NEW.append(i.split(" "))
    print(NEW)
    if len(NEW[0]) >= 7:
        for i in range(len(NEW)):
            for j in range(len(NEW[0])):
                try:
                    a,b = NEW[0][j].split(":")
                except:
                    a,b = NEW[0][j].split("\n")
                    a,b = a.split(":"),b.split(":")
                    a,b = a[0],b[0]
                    if b != 'cid':
                        pass
                    else:
                        break
                    FINAL.append(NEW[0])
                if a !=
                
            #FINAL.append(NEW[0])
    break

print(FINAL)

