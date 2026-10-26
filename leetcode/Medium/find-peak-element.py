// Problem: Find Peak Element
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-peak-element/
// Solved on: 2026-10-26T18:55:12.911Z

class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len (nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if left == right:
                return right
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid