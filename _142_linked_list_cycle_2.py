"""
142. Linked List Cycle II

Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.

Follow up:
Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            # Here slow = fast = meeting point (M)
            # Use two pointers each begin at head and M, they will meet at entry.
            entry = head
            while slow is not entry:
                slow = slow.next
                entry = entry.next
            return entry

        except:
            return None
        