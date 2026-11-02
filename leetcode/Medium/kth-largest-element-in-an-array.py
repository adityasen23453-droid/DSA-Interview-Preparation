// Problem: Kth Largest Element in an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
// Solved on: 2026-11-02T11:53:24.514Z

# Using random so that we can handle the below edge case
import random

class Solution(object):
    def findKthLargest(self, nums, k):
        left = 0
        right = len(nums) - 1
        target = len(nums) - k

        while left <= right:
            pivot = nums[random.randint(left, right)]

            i = left
            j = left
            end = right

            while j <= end:
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1

                elif nums[j] > pivot:
                    nums[j], nums[end] = nums[end], nums[j]
                    end -= 1

                else:
                    j += 1

            if target < i:
                right = i - 1

            elif target > end:
                left = end + 1

            else:
                return nums[target]



# Using Quickselect Method
# Fail in edge cases where u will have thousands on duplicate numbers
# Space Complexity: O(1)

# class Solution(object):
#     def findKthLargest(self, nums, k):
#         left = 0
#         right = len(nums) - 1
#         target = len(nums) - k
#
#         while left <= right:
#             pivot = nums[right]
#             i = left
#             j = left
#
#             while j < right:
#                 if nums[j] < pivot:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     i += 1
#                     j += 1
#                 else:
#                     j += 1
#
#             nums[i], nums[right] = nums[right], nums[i]
#
#             if i == target:
#                 return nums[i]
#             elif i < target:
#                 left = i + 1
#             else:
#                 right = i - 1