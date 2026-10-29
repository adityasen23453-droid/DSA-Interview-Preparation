// Problem: Relative Sort Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/relative-sort-array/
// Solved on: 2026-10-29T09:45:49.831Z

# Using Append method
class Solution (object):
 def relativeSortArray(self , arr1 , arr2):
      result = []
      arr1.sort()
      for i in range(len(arr2)):
        while arr2[i] in arr1:
            result.append(arr2[i])
            arr1.remove(arr2[i])
      for i in range(len(arr1)):
            result.append(arr1[i])
      return result