// Problem: Valid Perfect Square
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/valid-perfect-square/
// Solved on: 2026-10-23T16:11:35.746Z

class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num
        answer = 0
        while left <= right :
            mid = (left + right)//2
            req = mid * mid
            if req == num :
                return True
            elif req > num :
                right = mid - 1
            else :
                left = mid + 1
        return False