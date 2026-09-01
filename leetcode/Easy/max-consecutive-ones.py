// Problem: Max Consecutive Ones
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/max-consecutive-ones/
// Solved on: 2026-09-01T11:58:53.149Z

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
      count = 0
      max = 0
      for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        if max < count:
            max = count
      return max
        