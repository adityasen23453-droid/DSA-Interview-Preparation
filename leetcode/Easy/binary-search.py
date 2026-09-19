// Problem: Binary Search
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/binary-search/
// Solved on: 2026-09-19T16:43:43.475Z

class Solution(object):
    def search(self, nums, target):
      left = 0
      right = len(nums)-1
      while left <= right :
        mid = (left + right)// 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
      return -1