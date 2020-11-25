def removeElement(nums, val):
    a = 0
    b = 0
    
    while a < len(nums):
        if nums[a] != val:
            nums[b] = nums[a]
            b += 1
        a += 1

    return b

# val = 2
# [0,1,2,2,3,0,4,2]