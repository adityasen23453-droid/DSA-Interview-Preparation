// Problem: Contains Duplicate II
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/contains-duplicate-ii/
// Solved on: 2026-08-31T18:15:41.382Z

class Solution():
   def containsNearbyDuplicate(self , nums , k):
       window = set()
       for i in range(len(nums)):
           if nums[i] in window:
              return True
           window.add(nums[i])
           if len(window)>k:
              window.remove(nums[i-k]) 
       return False