# Arrays (1)

This week we will start to investigate algorithms about Arrays. There will be 3 questions in total:
2 *Easy* questions and 1 *Medium* question. Good luck!

## Question 1: Two Sum (Easy - 1)
**Question**:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

**Examples**:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
```
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
**Constraints**: 
* 2 <= nums.length <= 105
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

## Question 2: Remove Duplicates from Sorted Array (Easy - 26)
**Question**:
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

**Clarification**: 
Confused why the returned value is an integer but your answer is an array? Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Internally you can think of this:
```
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```
**Examples**:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
```

```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values are set beyond the returned length.
```

**Constraints**: 
* 0 <= nums.length <= 3 * 104
* -104 <= nums[i] <= 104
* nums is sorted in ascending order.

## Question 3: Container With Most Water (Medium - 11)
**Question**:
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

**Examples**:
![q2](./question_2.jpg)
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
```
```
Input: height = [1,1]
Output: 1
```
```
Input: height = [4,3,2,1,4]
Output: 16
```
```
Input: height = [1,2,1]
Output: 2
```

**Constraints**: 
* n = height.length
* 2 <= n <= 3 * 104
* 0 <= height[i] <= 3 * 104
