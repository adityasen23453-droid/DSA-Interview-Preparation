// Problem: Longest Substring Without Repeating Characters
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Solved on: 2026-09-02T17:23:01.976Z

class Solution:
  def lengthOfLongestSubstring(self,s):
      left = 0
      right = 0
      window = set()
      max_length = 0
      k = 0
      for right in range(len(s)):
         while s[right]  in window:
              window.remove(s[left])
              left += 1
         window.add(s[right])
         k = right - left + 1
         max_length = max(max_length,k)
      return max_length
           