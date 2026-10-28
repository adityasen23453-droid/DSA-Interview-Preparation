// Problem: Sort Array By Parity
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-array-by-parity/
// Solved on: 2026-10-28T17:13:12.787Z

class Solution(object):
    def sortArrayByParity(self, nums):
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] % 2 != 0 and nums[j] % 2 == 0:
                nums[i] , nums[j] = nums[j] , nums[i]
                i += 1
                j -= 1
            elif nums[i] % 2 == 0:
                i += 1
            else :
                j -= 1
                
        return nums         