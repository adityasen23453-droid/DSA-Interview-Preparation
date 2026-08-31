// Problem: Contains Duplicate II
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/contains-duplicate-ii/
// Solved on: 2026-08-31T18:19:55.463Z

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last = {}

        for i, num in enumerate(nums):
            if num in last and i - last[num] <= k:
                return True

            last[num] = i

        return False