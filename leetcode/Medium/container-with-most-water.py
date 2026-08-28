// Problem: Container With Most Water
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/container-with-most-water/
// Solved on: 2026-08-28T08:15:32.110Z

class Solution:
  def maxArea(self,height):
     left = 0
     right = len(height)-1
     k = 0
     while left < right:
        width = right - left
        max_area = width * min(height[left],height[right])
        if height[left] < height[right]:
           left += 1
        else:
           right -= 1
        if k < max_area:
           k = max_area
     return k
        