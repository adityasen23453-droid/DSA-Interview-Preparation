// Problem: Subarray Sums Divisible by K
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/subarray-sums-divisible-by-k/
// Solved on: 2026-08-23T14:54:15.536Z

class Solution:
    def subarraysDivByK(self, nums, k):
        total = 0
        count = 0
        result = {0: 1}

        for num in nums:
            total += num
            remainder = total % k

            if remainder in result:
                count += result[remainder]

            result[remainder] = result.get(remainder, 0) + 1

        return count