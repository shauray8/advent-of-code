nums = [11,33,33,11,33,11]
freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

ans = []
for i in freq.keys():
    if freq[i] > len(nums)/3:
        ans.append(i)
print(ans)
