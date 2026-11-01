// Problem: Largest Number
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/largest-number/
// Solved on: 2026-11-01T16:15:22.862Z

# Time complexity O(nlogn * k )
#k is refered to max number of digits in a number
class Solution(object):
   def largestNumber(self , nums):
       from functools import cmp_to_key 
       #Used so that python can understand the compare function
       for i in range(len(nums)):
        nums[i] = str(nums[i])
       def compare(a,b):
        if a + b > b + a :
            return -1
        elif a+ b < b + a:
            return 1 
        else :
            return 0
       nums.sort( key = cmp_to_key(compare))
       if nums[0] == "0" :
            return "0"
       return "".join(nums)