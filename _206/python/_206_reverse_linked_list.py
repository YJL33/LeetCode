"""
206. Reverse Linked List

Reverse a singly linked list.

A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Iterative method, T:O(n), S:O(1)
        prev = None
        while head:
            pointer = head
            head = head.next
            pointer.next = prev
            prev = pointer

        return prev         # Here head == None!
