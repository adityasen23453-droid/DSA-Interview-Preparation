// Problem: Find Minimum in Rotated Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Solved on: 2026-10-26T17:31:00.499Z

class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if left == right :
                return nums[left]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[right]:
                right = mid -1
            else :
                left = mid + 1