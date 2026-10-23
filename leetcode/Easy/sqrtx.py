// Problem: Sqrt(x)
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sqrtx/
// Solved on: 2026-10-23T15:16:23.271Z

class Solution(object):
    def mySqrt(self, x):
        answer = 0
        left = 0
        right = x
        while left <= right:
            mid = (left + right)//2
            req = mid * mid
            if req <= x:
                need = mid
                left = left + 1
            else :
                right = mid - 1
        return max(answer,need)
                
        