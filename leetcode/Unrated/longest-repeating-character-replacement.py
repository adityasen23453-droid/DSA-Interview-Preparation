// Problem: Longest Repeating Character Replacement
// Platform: leetcode
// Rating/Difficulty: Unrated
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/longest-repeating-character-replacement/
// Solved on: 2026-09-10T04:05:27.917Z

class Solution:
    def characterReplacement(self, s, k):

        count = {}

        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):

            # 1. Add character
            if s[right] not in count:
                count[s[right]] = 0

            count[s[right]] += 1

            # 2. Find highest frequency
            max_freq = max(max_freq, count[s[right]])

            # 3. Find window size
            window_size = right - left + 1

            # 4. Find how many replacements are needed
            replacements = window_size - max_freq

            # 5. If too many replacements are needed,
            #    move left
            while replacements > k:

                count[s[left]] -= 1
                left += 1

                window_size = right - left + 1
                replacements = window_size - max_freq

            # 6. Store largest valid window
            max_length = max(max_length, window_size)

        return max_length