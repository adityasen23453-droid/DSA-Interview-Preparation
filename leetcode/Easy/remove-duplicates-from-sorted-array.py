// Problem: Remove Duplicates from Sorted Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
// Solved on: 2026-08-22T05:48:37.658Z

class Solution(object):
    def removeDuplicates (self, nums):
        slow = 0
        fast = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            else:
                fast += 1
        return slow + 1