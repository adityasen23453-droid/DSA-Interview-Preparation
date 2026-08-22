// Problem: Single Number
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/single-number/
// Solved on: 2026-08-22T05:45:59.305Z

class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for i in nums:
            result = result^i
        return result