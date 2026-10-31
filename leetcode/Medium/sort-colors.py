// Problem: Sort Colors
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-colors/
// Solved on: 2026-10-31T09:17:21.174Z

class Solution(object):
    def sortColors(self , nums):
       i = 0
       j = 0
       k = len(nums) - 1
       while j <=k :
           if nums[j] == 2 :
              nums[j] , nums[k] = nums[k] , nums[j]
              k -= 1
           elif nums[j] == 0:
              nums[i],nums[j] = nums[j], nums[i]
              i += 1
              j += 1
           else :
              j += 1
       return nums