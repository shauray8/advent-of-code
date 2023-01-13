nums = [2,2,1,1,1,2,2]
hashmap = {}

for i in range(len(nums)):
    hashmap.update({nums[i], }) 

print(hashmap)
