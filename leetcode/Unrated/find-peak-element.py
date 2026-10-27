// Problem: Find Peak Element
// Platform: leetcode
// Rating/Difficulty: Unrated
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-peak-element/
// Solved on: 2026-10-27T08:59:03.157Z

# 2nd way

class Solution(object):
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if left == right:
                return left

            elif mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
                else:
                    left = mid + 1

            elif mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
                else:
                    right = mid - 1

            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            elif nums[mid] < nums[mid + 1]:
                left = mid + 1

            else:
                right = mid