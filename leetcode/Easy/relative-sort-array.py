// Problem: Relative Sort Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/relative-sort-array/
// Solved on: 2026-10-29T09:29:03.753Z

class Solution (object):
 def relativeSortArray(self , arr1 , arr2):
      order = {}
      for num in range(len(arr2)):
          order[arr2[num]] = num
      def sort_key(num):
          new = {}
          if num in order:
             new = (0 , order[num])
          else :
             new = (1 , num)
          return new
      arr1.sort(key = sort_key)
      return arr1