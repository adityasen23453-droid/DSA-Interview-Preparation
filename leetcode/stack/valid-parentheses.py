// Problem: Valid Parentheses
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/valid-parentheses/
// Solved on: 2026-08-22T05:49:24.433Z

class Solution(object):
    def isValid(self, s):
        stack = []
        for ch in s:
            if ch == '{' or ch == '[' or ch == '(':
                stack.append(ch)
            elif ch == '}':
                if not stack :
                    return False
                elif stack[-1] != '{':
                    return False
                stack.pop()
            elif ch == ']':
                if not stack:
                    return False
                elif stack[-1] != '[':
                    return False
                stack.pop()
            elif ch == ')':
                if not stack:
                    return False
                elif stack[-1] != '(':
                    return False
                stack.pop()
        return len(stack) == 0