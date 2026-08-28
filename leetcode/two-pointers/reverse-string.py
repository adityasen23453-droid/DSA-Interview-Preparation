// Problem: Reverse String
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/reverse-string/
// Solved on: 2026-08-22T05:48:09.456Z

class Solution(object):
    def reverseString(self , s):
        left = 0
        right = len(s) -1 
        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -=1
            