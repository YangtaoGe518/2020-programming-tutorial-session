# Moore Volting method

# major = 0
# count = 0
# i = 0 // pointer
# [1,2,5,9,5,9,5,5,5]
#  major = nums[i]

def majorityElement(nums):
    major = 0
    count = 0

    if not nums:
        return -1

    for num in nums:
        if count == 0:
            major = num
            count = count + 1
        else: 
            if num == major:
                count = count + 1
            else:
                count = count - 1

    if count == 0:
        return -1
    
    identify = 0
    for num in nums:
        if num == major:
            identify = identify + 1
            if identify > len(nums) / 2:
                return major
    
    return -1

print(majorityElement([1,2,5,9,5,9,5,5,5]))
