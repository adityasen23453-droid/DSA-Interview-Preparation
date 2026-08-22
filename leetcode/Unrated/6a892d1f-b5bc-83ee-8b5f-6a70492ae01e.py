// Problem: Connect LeetCode GitHub Career Impact
// Platform: leetcode
// Language: Python3
// Verdict: Accepted
// URL: https://chatgpt.com/c/6a892d1f-b5bc-83ee-8b5f-6a70492ae01e
// Solved on: 2026-08-22T05:33:28.549Z

class Solution:
    def isArmstrong(self, n):
        num = str(n)
        sum = 0
        gum = len(num)
        i = 0
        while i < gum:
            k = int(num[i])**gum
            sum = sum + k
            i += 1
        if sum == n :
            return True
        else:
            return False
