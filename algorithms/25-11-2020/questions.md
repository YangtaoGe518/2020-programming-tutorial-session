# Arrays (2)

This week we will still investigate algorithms about Arrays. There will be 3 questions in total:
2 *Easy* questions and 1 *Medium* question. Good luck!

## Question 1: Remove Elements (Easy - 27)
**Question**:
Given an array nums and a value val, remove all instances of that value in-place and return the new length. Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory. The order of elements can be changed. It doesn't matter what you leave beyond the new length.

**Clarification**: 
Confused why the returned value is an integer but your answer is an array? Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well. Internally you can think of this:

```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```

**Examples**:
```
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or nums = [2,3,0,0], your answer will be accepted.
```

```
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3]
Explanation: Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4. Note that the order of those five elements can be arbitrary. It doesn't matter what values are set beyond the returned length.
```

**Constraints**: 
* 0 <= nums.length <= 100
* 0 <= nums[i] <= 50
* 0 <= val <= 100

## Question 2: Find Majority Element (Easy - interview.17.10)
**Question**:
A majority element is an element that makes up more than half of the items in an array. Given a positive integers array, find the majority element. If there is no majority element, return -1. 

**Examples**:
```
Input: [1,2,5,9,5,9,5,5,5]
Output: 5
```
```
Input: [3,2]
Output: -1
```
```
Input: [2,2,1,1,1,2,2]
Output: 2
```

## Question 3: Next Permutation (Medium - 31)
**Question**:
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).The replacement must be in place and use only constant extra memory.
**Examples**:
```
Input: nums = [1,2,3]
Output: [1,3,2]
```
```
Input: nums = [3,2,1]
Output: [1,2,3]
```
```
Input: nums = [1,1,5]
Output: [1,5,1]
```

**Constraints**: 
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 100