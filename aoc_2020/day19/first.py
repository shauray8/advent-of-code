lis = []
w = open('data.txt','r')
lis.append(w.read())
lis = lis[0].split("\n\n")

rules, message = [lis[0].split("\n")], [lis[1].split("\n")]
message.pop(-1)

ruledict = {}
for i in range(len(rules)):
    ruledict.update({rules[0][i].split(":")[0],rules[0][i].split(":")[0]})

print(ruledict)
