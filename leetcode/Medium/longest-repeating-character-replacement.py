// Problem: Longest Repeating Character Replacement
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-repeating-character-replacement/
// Solved on: 2026-09-09T17:40:25.997Z

class Solution:
    def characterReplacement(self, s, k):

        count = {}

        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):

            # Add current character to frequency map
            count[s[right]] = count.get(s[right], 0) + 1

            # Update maximum frequency
            max_freq = max(max_freq, count[s[right]])

            # Number of characters we need to replace
            window_size = right - left + 1
            replacements = window_size - max_freq

            # If replacements exceed k,
            # shrink the window
            while replacements > k:

                count[s[left]] -= 1
                left += 1

                window_size = right - left + 1
                replacements = window_size - max_freq

            # Current window is valid
            max_length = max(max_length, right - left + 1)

        return max_length