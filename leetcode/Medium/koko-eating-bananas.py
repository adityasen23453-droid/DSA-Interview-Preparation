// Problem: Koko Eating Bananas
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/koko-eating-bananas/
// Solved on: 2026-10-28T05:18:52.513Z


class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += (pile + mid - 1) // mid

                if hours > h:
                    break

            if hours <= h:
                right = mid
            else:
                left = mid + 1

        return right
