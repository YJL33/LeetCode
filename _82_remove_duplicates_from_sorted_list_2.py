"""
82. Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lastvalid, lastvalid.next = ListNode(0), head       # record last valid one
        dummyhead = lastvalid                               # pos of head
        while head and head.next:
            if head.val != head.next.val:                   # move on
                lastvalid, head = head, head.next
            else:                                           # delete all nodes with this val
                cursor = head.next
                while cursor and cursor.val == head.val:    # go on until != val (or end)
                    cursor = cursor.next
                lastvalid.next, head = cursor, cursor

        return dummyhead.next