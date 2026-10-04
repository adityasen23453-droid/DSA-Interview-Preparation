// Problem: Find Smallest Letter Greater Than Target
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/find-smallest-letter-greater-than-target/
// Solved on: 2026-10-04T15:15:19.319Z

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1
        ans_idx = len(letters)
        
        while left <= right:
            mid = (left + right) // 2
            if letters[mid] > target:
                ans_idx = mid
                right = mid - 1
            else:
                left = mid + 1
                
        if ans_idx == len(letters):
            return letters[0]
            
        return letters[ans_idx]
        