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
        # Recursive method, T: O(n)
        return self.helper(head)

    def helper(self, node, prev=None):
        if not node: return prev
        cursor = node.next
        node.next = prev
        return self.helper(cursor, node)