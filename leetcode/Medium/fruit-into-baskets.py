// Problem: Fruit Into Baskets
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/fruit-into-baskets/
// Solved on: 2026-09-04T16:15:32.375Z

class Solution :
    def totalFruit(self, fruits):
        left = 0
        right = 0
        count = {}
        max_length = 0
        for right in range (len(fruits)):
            if fruits[right] not in count:
               count[fruits[right]] = 0
            count[fruits[right]] += 1
            while len(count) > 2:
                 count[fruits[left]] -= 1
                 if count[fruits[left]] == 0:
                    del count[fruits[left]]
                 left += 1
            k = right - left + 1
            if max_length < k :
                max_length = k
        return max_length