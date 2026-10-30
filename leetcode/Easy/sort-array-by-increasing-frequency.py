// Problem: Sort Array by Increasing Frequency
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-array-by-increasing-frequency/
// Solved on: 2026-10-30T17:59:48.683Z

class Solution(object):
    def frequencySort(self , nums):
        freq = {}
        for i in nums:
            if i not in freq :
                freq[i] = 1
            else :
                freq[i] += 1
        nums.sort(key = lambda x : (freq[x] , -x))
        return nums