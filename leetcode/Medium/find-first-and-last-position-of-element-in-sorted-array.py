// Problem: Find First and Last Position of Element in Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// Solved on: 2026-10-04T15:17:45.664Z

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def lower_bound(nums, target):
            left, right = 0, len(nums) - 1
            ans = len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        def upper_bound(nums, target):
            left, right = 0, len(nums) - 1
            ans = len(nums)
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        start = lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
            
        end = upper_bound(nums, target) - 1
        return [start, end]

        
        