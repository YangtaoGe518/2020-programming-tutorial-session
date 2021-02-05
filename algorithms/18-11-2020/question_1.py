
## O(N^2)
def twoSum_1 (nums, target):
    size = len(nums)
    for i in range(size):
        for j in range (i+1, size):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

## O(n + nlogn) ~ O(2n) = O(N)
#   2  7  11  13  15   19 
#      i       j    

## O(N)
## target - x take longer time
def twoSum_2 (nums, target):
    hashtable = dict()
    for i, num in enumerate(nums):
        if target - num in hashtable:
            return [hashtable[target - num], i]
        hashtable[num] = i
    return []

   

nums =  [2,7,11,15]
target = 20

print(twoSum_2(nums, target))