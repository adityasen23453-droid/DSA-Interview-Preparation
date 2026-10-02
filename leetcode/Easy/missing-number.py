// Problem: Missing Number
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/missing-number/
// Solved on: 2026-10-02T14:30:27.420Z

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i :
                return i
        return len(nums)