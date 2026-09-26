// Problem: Search Insert Position
// Platform: leetcode
// Rating/Difficulty: Unrated
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/search-insert-position/
// Solved on: 2026-09-26T03:00:58.862Z

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return left