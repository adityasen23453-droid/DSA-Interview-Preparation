// Problem: Permutation in String
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/permutation-in-string/
// Solved on: 2026-09-05T17:49:32.212Z

class Solution:
    def checkInclusion(self, s1, s2):

        # If s1 is longer, permutation cannot exist in s2
        if len(s1) > len(s2):
            return False

        count1 = {}
        count2 = {}

        # -----------------------------------
        # Step 1: Frequency of characters in s1
        # -----------------------------------
        for ch in s1:
            count1[ch] = count1.get(ch, 0) + 1

        # -----------------------------------
        # Step 2: Create the first window
        # -----------------------------------
        for i in range(len(s1)):
            ch = s2[i]
            count2[ch] = count2.get(ch, 0) + 1

        # -----------------------------------
        # Step 3: Check first window
        # -----------------------------------
        if count1 == count2:
            return True

        # -----------------------------------
        # Step 4: Start sliding the window
        # -----------------------------------
        left = 0

        for right in range(len(s1), len(s2)):

            # Add new character entering the window
            ch = s2[right]
            count2[ch] = count2.get(ch, 0) + 1

            # Remove character leaving the window
            old = s2[left]
            count2[old] -= 1

            # If frequency becomes 0, remove the key
            if count2[old] == 0:
                del count2[old]

            # Move left pointer
            left += 1

            # Check if current window is a permutation
            if count1 == count2:
                return True

        return False