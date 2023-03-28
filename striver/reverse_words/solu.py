s = "this is an amazing program"
ans = ""

for i in s.split(" ")[::-1]:
    ans += i+" "

print(ans.strip())

