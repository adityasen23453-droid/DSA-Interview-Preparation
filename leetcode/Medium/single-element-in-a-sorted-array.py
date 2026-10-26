// Problem: Single Element in a Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/single-element-in-a-sorted-array/
// Solved on: 2026-10-26T17:08:58.442Z

class Solution(object):
    def singleNonDuplicate(self, nums):
       left = 0
       right = len(nums) - 1
       while left <= right :
        mid = (left + right)//2
        if left == right:
            return nums[left]
        elif nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        elif mid % 2 == 0 and nums[mid] == nums[mid + 1]:
            left = mid + 1
        elif mid % 2 == 1 and nums[mid] == nums[mid - 1]:
            left = mid + 1
        else :
            right = mid - 1