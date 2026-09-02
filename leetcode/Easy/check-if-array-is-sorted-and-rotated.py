// Problem: Check if Array Is Sorted and Rotated
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/
// Solved on: 2026-09-02T15:08:24.511Z

class Solution:
   def check(self , nums) :
       count = 0
       for i in range(len(nums)):
          if nums[i] > nums[(i + 1) % len(nums)]:
                 count += 1
       return count <= 1