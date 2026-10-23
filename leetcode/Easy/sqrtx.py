// Problem: Sqrt(x)
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sqrtx/
// Solved on: 2026-10-23T15:19:05.230Z

# corrected the required integer storing  logic

class Solution(object):
    def mySqrt(self, x):
        answer = 0
        left = 0
        right = x
        while left <= right:
            mid = (left + right)//2
            req = mid * mid
            if req <= x:
                answer = mid
                left = mid + 1
            else :
                right = mid - 1
        return answer
                
        