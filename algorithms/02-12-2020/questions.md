# Two Pointers

This week we will do further investigations on two pointer method that we used last two weeks. There will be 3 questions in total:
1 *Easy* questions and 2 *Medium* question. Good luck!

## Question 1: Linked List Circle (Easy - 141)
**Question**:
Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter. Return true if there is a cycle in the linked list. Otherwise, return false.

**Examples**:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
```
```
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
```
```
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
```
**Constraints**: 
* The number of the nodes in the list is in the range [0, 10^4].
* -10^5 <= Node.val <= 10^5
* pos is -1 or a **valid index** in the linked-list.

## Question 2: Remove Nth Node From End of List (Medium - 19)
**Question**:
Given the head of a linked list, remove the nth node from the end of the list and return its head. Follow up: Could you do this in one pass?

**Examples**:
```
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
```
```
Input: head = [1], n = 1
Output: []
```
```
Input: head = [1,2], n = 1
Output: [1]
```
**Constraints**: 
* The number of nodes in the list is sz.
* 1 <= sz <= 30
* 0 <= Node.val <= 100
* 1 <= n <= sz

## Question 3: 3 sum Closest (Medium - 16)
**Question**:
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

**Examples**:
```
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
**Constraints**: 
* 3 <= nums.length <= 10^3
* -10^3 <= nums[i] <= 10^3
* -10^4 <= target <= 10^4
