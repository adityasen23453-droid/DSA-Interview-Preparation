// Problem: Max Consecutive Ones III
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/max-consecutive-ones-iii/
// Solved on: 2026-09-03T17:33:08.971Z

class Solution:
   def longestOnes(self , nums, k):
       left = 0 
       right = 0
       max_count = 0
       zero_count = 0

       for right in range(len(nums)):
           if nums[right] == 0:
              zero_count += 1

              while zero_count > k:
                    if nums[left] == 0:
                         zero_count -= 1
                    left += 1

           m = right - left + 1
           max_count = max(m,max_count)

       return max_count