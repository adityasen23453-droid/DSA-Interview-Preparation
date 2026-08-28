// Problem: Move Zeroes
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/move-zeroes/
// Solved on: 2026-08-22T05:47:55.973Z

class Solution(object):
    def moveZeroes(self, nums):
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        while i < len(nums):
            nums[i] = 0
            i +=1