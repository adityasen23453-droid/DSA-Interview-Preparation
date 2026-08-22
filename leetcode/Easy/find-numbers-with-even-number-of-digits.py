// Problem: Find Numbers with Even Number of Digits
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
// Solved on: 2026-08-22T05:51:44.278Z

class Solution(object):
    def findNumbers(self, nums):
        count = 0
        for i in nums:
            if len(str(i))%2==0:
                count += 1
        return count