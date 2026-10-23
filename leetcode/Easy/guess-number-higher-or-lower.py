// Problem: Guess Number Higher or Lower
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/guess-number-higher-or-lower/
// Solved on: 2026-10-23T13:46:27.141Z

class Solution(object):
    def guessNumber(self, n):
        left = 1
        right = n 
        while left <= right :
            mid = (left + right)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == - 1 :
                right = mid - 1
            else:
                left = mid + 1
            