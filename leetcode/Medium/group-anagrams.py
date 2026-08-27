// Problem: Group Anagrams
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/group-anagrams/
// Solved on: 2026-08-27T13:53:00.971Z

class Solution:
    def groupAnagrams(self, strs):
        result = {}

        for word in strs:
            key = "".join(sorted(word))

            if key in result:
                result[key].append(word)
            else:
                result[key] = [word]

        return list(result.values())