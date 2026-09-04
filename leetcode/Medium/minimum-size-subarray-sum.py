// Problem: Minimum Size Subarray Sum
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/minimum-size-subarray-sum/
// Solved on: 2026-09-04T15:40:46.838Z

class Solution:
    def minSubArrayLen(self, target, nums):
        left = 0
        arr_sum = 0
        min_len = float('inf')

        for right in range(len(nums)):
            arr_sum += nums[right]

            while arr_sum >= target:
                k = right - left + 1

                if min_len > k:
                    min_len = k

                arr_sum -= nums[left]
                left += 1

        if min_len == float('inf'):
            return 0

        return min_len