// Problem: Two Sum
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/two-sum/
// Solved on: 2026-08-22T05:44:00.974Z

class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        i = 0
        for num in nums:

            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

            i += 1