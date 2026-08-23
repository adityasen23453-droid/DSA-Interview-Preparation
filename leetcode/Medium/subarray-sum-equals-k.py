// Problem: Subarray Sum Equals K
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/subarray-sum-equals-k/
// Solved on: 2026-08-23T07:44:01.229Z

class Solution:
    def subarraySum(self, nums, k):
        total = 0
        count = 0
        result = {0: 1}

        for num in nums:
            total += num
            target = total - k

            if target in result:
                count += result[target]

            result[total] = result.get(total, 0) + 1

        return count