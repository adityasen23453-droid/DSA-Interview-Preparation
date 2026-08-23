// Problem: Longest Consecutive Sequence
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-consecutive-sequence/
// Solved on: 2026-08-23T16:09:28.600Z

class Solution:
    def longestConsecutive(self, nums):
        req = set(nums)
        count = 0
        k = 0

        for num in req:
            if num - 1 not in req:
                current = num
                count = 1

                while current + 1 in req:
                    count += 1
                    current += 1

                if k < count:
                    k = count

        return k