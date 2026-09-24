// Problem: Reverse Linked List
// Platform: leetcode
// Rating/Difficulty: Easy
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/reverse-linked-list/
// Solved on: 2026-09-24T16:33:10.239Z

class Solution(object):
    def reverseList(self, head):

        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev

            prev = curr
            curr = next_node

        return prev