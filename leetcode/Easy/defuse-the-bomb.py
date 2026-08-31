// Problem: Defuse the Bomb
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/defuse-the-bomb/
// Solved on: 2026-08-31T19:20:04.199Z

class Solution:
    def decrypt(self, code, k):

        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        # k > 0
        if k > 0:
            window_sum = 0

            # first window
            for j in range(1, k + 1):
                window_sum += code[j % n]

            for i in range(n):
                result[i] = window_sum

                # remove outgoing
                window_sum -= code[(i + 1) % n]

                # add incoming
                window_sum += code[(i + k + 1) % n]

        # k < 0
        else:
            k = -k
            window_sum = 0

            # first window: previous k elements
            for j in range(1, k + 1):
                window_sum += code[-j]

            for i in range(n):
                result[i] = window_sum

                # remove outgoing
                window_sum -= code[(i - k) % n]

                # add incoming
                window_sum += code[i % n]

        return result