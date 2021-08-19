lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n")
lis.pop(-1)
#print(lis)

temp = ["5 + (8 * 3 + 9 + 3 * 4 * 3)"]

a = []
for i in temp[0].split(' '):
    a.append(i)


import re

class num(int):
    def __sub__(self,b):
        return num(int(self)*int(b))

    def __add__(self, b):
        return num(int(self) + int(b))

    def __mul__(self, b):
        return num(int(self) + int(b))

s = 0
for row in lis:
    row = row.replace("*","-")
    row = row.replace("+","*")
    row = re.sub('(\d+)',r'num(\1)', row)
    s += eval(row)
print(s)
