"""
24. Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return []
        if not head.next: return head

        new = head.next         # beginning of new linked-list
        prev = self             # end of new linked-list

        while head and head.next:           # loop while there's still elements need to swap
            cur = head.next.next            # point to next pair
            prev.next = head.next           # extend the tail 1 node (not when 1st pair)
            head.next.next = head           # extend the tail 1 more node
            head.next = cur                 # extend the tail 1 more node (this may be None)
            prev = head                     # track the position of tail
            head = cur                      # move to next pair

        return new
