// Problem: Contains Duplicate
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/contains-duplicate/
// Solved on: 2026-08-22T05:51:29.602Z

class Solution(object):
    def containsDuplicate(self , nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
