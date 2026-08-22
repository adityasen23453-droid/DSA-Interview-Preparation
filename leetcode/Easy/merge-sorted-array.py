// Problem: Merge Sorted Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-sorted-array/
// Solved on: 2026-08-22T05:46:36.087Z

class Solution(object):

   def merge(self , nums1,m,nums2,n):

      i = m-1

      j= n-1

      k = m+n -1

      while j >=0: 

           if i < 0 or nums2[j] > nums1[i]:

                nums1[k] = nums2[j]

                j -= 1

                k -= 1

           else :

               nums1[k] = nums1[i]

               i -=1

               k -= 1



               