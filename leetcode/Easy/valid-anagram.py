// Problem: Valid Anagram
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/valid-anagram/
// Solved on: 2026-08-22T05:51:14.642Z

class Solution(object):
    def isAnagram(self, s, t):

        # Quick rejection
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters from s
        for ch in s:
            if ch not in freq:
                freq[ch] = 0
            freq[ch] += 1

        # Remove characters from t
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1

        # Final check
        for value in freq.values():
            if value != 0:
                return False

        return True