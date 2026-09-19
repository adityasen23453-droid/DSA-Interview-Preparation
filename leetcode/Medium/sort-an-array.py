// Problem: Sort an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-an-array/
// Solved on: 2026-09-19T16:05:07.550Z

class Solution(object):
    def sortArray(self, nums):
        def merge_sort(nums):
            l = len(nums)

            if l <= 1:
                return nums
            mid = l//2
            left_half = nums[:mid]
            right_half = nums[mid:]
            left = merge_sort(left_half)
            right = merge_sort(right_half)
            return merge_arr(left,right)

        def merge_arr(left,right):
            result = []
            i , j =  0 , 0
            m , n = len(left) , len(right)

            while i < m and j < n:
                if left[i] < right[j]:
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j += 1
            while i < m:
                result.append(left[i])
                i += 1
            while j < n :
                result.append(right[j])
                j += 1

            return result

        return merge_sort(nums)