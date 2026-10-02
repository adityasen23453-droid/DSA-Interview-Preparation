// Problem: Rotate Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/rotate-array/
// Solved on: 2026-10-02T05:09:53.355Z

# k%n for handling edge case & proper rotation like 11 % 4 where k = 11 ans len(nums) = 4

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k:] + nums[:n-k]
        return nums
        