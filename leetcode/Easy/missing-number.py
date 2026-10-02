// Problem: Missing Number
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/missing-number/
// Solved on: 2026-10-02T14:32:43.630Z

class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)): 
            if nums[i] != i :  #check for all values with there index
                return i
        return len(nums)  # return the len of the array if all the values matches becz in [0,1,2] only 3 would be missing that is out of the bound