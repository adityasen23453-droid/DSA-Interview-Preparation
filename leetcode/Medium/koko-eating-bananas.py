// Problem: Koko Eating Bananas
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/koko-eating-bananas/
// Solved on: 2026-10-28T05:11:38.401Z

#With using max function
class Solution(object):
   def minEatingSpeed(self , piles , h):
      left = 1
      right = max(piles)
      while left < right :
          mid = (left + right) //2
          total_time = 0
          for i in range(len(piles)):
              if piles[i] % mid == 0 :
                 hours = piles[i]//mid
                 total_time = total_time + hours
              else :
                 hours = piles[i]//mid + 1
                 total_time = total_time + hours
          if total_time <= h:
             right = mid
          else :
             left = mid + 1
      return right
             