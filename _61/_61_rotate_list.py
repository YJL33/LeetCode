"""
61. Rotate List

Given a list, rotate the list to the right by k places,
where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1. count the length of list
        # 2. cut at desired spot
        # 3. connect tail to head

        if not head or k==0: return head

        counter = 0                                 # length of linked-list
        dummy, dummy.next = ListNode(0), head       # dummy head
        tail = dummy                                # tail of scanned area (linked-list)

        while tail.next:
            counter += 1
            tail = tail.next

        k = k%counter                               # k may exceed the length

        spot = counter - k
        prev, cursor = dummy, dummy.next
        if spot == 0 or spot == counter: return cursor      # must have this line

        while spot:
            prev, cursor = cursor, cursor.next
            spot -= 1

        # Now 2nd half beginning at cursor, simply rotate it here
        prev.next, tail.next = None, dummy.next

        return cursor