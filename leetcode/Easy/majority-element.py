// Problem: Majority Element
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/majority-element/
// Solved on: 2026-08-22T05:45:06.109Z

class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

            if count[num] > len(nums) // 2:
                return num