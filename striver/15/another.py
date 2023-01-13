nums = [2,2,1,1,1,2,2]
hashmap = {}

for i in range(len(nums)):
    if nums[i] in hashmap:
        hashmap[nums[i]] += 1
    else:
        hashmap[nums[i]] = 1

max_freq = max(hashmap.values())
list1 = list(hashmap.keys())
list2 = list(hashmap.values())
position = list2.index(max_freq)
print(list1[position])

