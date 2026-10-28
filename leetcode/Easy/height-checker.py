// Problem: Height Checker
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/height-checker/
// Solved on: 2026-10-28T16:27:42.458Z

class Solution(object):
    def heightChecker(self, heights):
        count = 0
        i = 0
        expected = sorted(heights)
        h = len(heights)
        while i < h :
            if heights[i] != expected[i]:
                count += 1
                i += 1
            else :
                i += 1
        return count