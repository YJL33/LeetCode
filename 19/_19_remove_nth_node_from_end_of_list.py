"""
19. Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev, dummy.next = dummy, head
        tail = self.isThisNodeNone(head, n)     # n nodes away from head

        while tail:                             # while it's not None ...
            prev, head, tail = head, head.next, tail.next      # everyone move one step forward

        prev.next = head.next                   # remove the head
        return dummy.next                       # return dmy.next

    def isThisNodeNone(self, node, n):
        while n > 0:
            node = node.next
            n -= 1
        return node