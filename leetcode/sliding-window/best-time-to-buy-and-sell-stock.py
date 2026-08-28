// Problem: Best Time to Buy and Sell Stock
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Solved on: 2026-08-22T05:46:12.593Z

class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        max = 0
        for i in range(0, len(prices)):
            if prices[i] < min:
                min = prices[i]
            k = prices[i] - min
            if k > max:
                max = k
        return max
        