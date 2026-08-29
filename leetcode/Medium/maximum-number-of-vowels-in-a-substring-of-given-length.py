// Problem: Maximum Number of Vowels in a Substring of Given Length
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
// Solved on: 2026-08-29T11:28:19.867Z

class Solution(object):
    def maxVowels(self, s, k):
        count = 0
        for i in range(k):
            if s[i] in "aeiou":
                count += 1
            max_vowel = count
        for i in range(k,len(s)):
            if s[i - k] in "aeiou":
                count -= 1
            if s[i] in "aeiou":
                count += 1
            if max_vowel < count:
                max_vowel = count
        return max_vowel
            
        