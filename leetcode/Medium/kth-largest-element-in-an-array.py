// Problem: Kth Largest Element in an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
// Solved on: 2026-11-02T06:33:03.979Z

#With sorting
class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        return nums[-k]        