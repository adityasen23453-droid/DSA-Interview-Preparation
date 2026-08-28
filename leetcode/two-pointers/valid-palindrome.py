// Problem: Valid Palindrome
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/valid-palindrome/
// Solved on: 2026-08-22T05:49:05.145Z

class Solution(object):
    def isPalindrome(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True 
        