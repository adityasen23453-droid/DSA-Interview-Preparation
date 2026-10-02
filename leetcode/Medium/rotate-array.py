// Problem: Rotate Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/rotate-array/
// Solved on: 2026-10-02T04:54:09.330Z

class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        old_nums = list(nums)
        for i in range(n):
            nums[i] = old_nums[(i-k)%n]
        return nums
        