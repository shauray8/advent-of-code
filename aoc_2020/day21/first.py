lis = []
w = open('data.input','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)

inc = []
alle = []

for i in range(len(lis)):
    a,b = lis[i].split("(contains ")
    inc.append(a)
    alle.append(b)

for i in range(len(inc)):
    for j in inc[i].split(" "):
        print(j)
        
