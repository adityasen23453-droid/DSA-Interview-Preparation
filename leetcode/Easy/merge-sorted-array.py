// Problem: Merge Sorted Array
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/merge-sorted-array/
// Solved on: 2026-10-31T06:30:50.630Z

# Two-pointers approach 
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:   #checks for last values nums1[k] & nums2[j]
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:  # Checks if the array is empty
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1