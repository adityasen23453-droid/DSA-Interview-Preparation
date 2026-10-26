// Problem: Search in Rotated Sorted Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
// Solved on: 2026-10-26T17:40:28.240Z

class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right)//2
            if nums[mid] == target :
                return mid
            elif nums[left] <= nums[mid] :
                if nums[left] <= target < nums [mid]:
                    right = mid - 1
                else :
                    left = mid + 1 
            else :
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else :
                    right = mid - 1
        return -1
                 