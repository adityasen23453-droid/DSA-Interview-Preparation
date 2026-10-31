// Problem: Sort an Array
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-an-array/
// Solved on: 2026-10-31T10:21:27.392Z

# Ans using merge sort 
# time complexity O(nlog(n))
#space complexity O(n)
class Solution(object):
    def sortArray(self, nums):
        i = 0
        j = 0
        temp = []
        mid =len(nums)//2
        if len(nums) == 1 :
            return nums
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        m = len(left)
        n = len(right)
        while i < m and j < n :
            if left[i] > right[j] :
                temp.append(right[j])
                j += 1
            else:
                temp.append(left[i])
                i += 1
        while i < m:
            temp.append(left[i])
            i += 1
        while j < n:
            temp.append(right[j])
            j += 1
        return temp