// Problem: Sort List
// Platform: leetcode
// Rating/Difficulty: Medium
// Language: python
// Verdict: Accepted
// URL: https://leetcode.com/problems/sort-list/
// Solved on: 2026-11-05T17:52:18.101Z


class Solution:
    def sortList(self, head):

        # Base case
        if head is None or head.next is None:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Step 2: Divide the list into two halves
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        # Step 3: Merge both sorted halves
        return self.merge(left, right)

    def merge(self, left, right):

        dummy = ListNode(0)
        current = dummy

        while left and right:

            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Attach remaining nodes
        if left:
            current.next = left

        if right:
            current.next = right

        return dummy.next

        