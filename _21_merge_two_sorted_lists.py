"""
21. Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Since l1 and l2 are already sorted, just merge l2 into l1.
        # T: O(L1+L2), O(1)
        if not l1 and l2: return l2
        if not l2 and l1: return l1
        if not l1 and not l2: return []
        
        if l1.val < l2.val: head = l1
        else: head = l2

        cursor1 = l1        # head of list-1
        cursor2 = l2        # head of list-2
        prev = None         # end of merged list

        while cursor2:
            temp2 = cursor2.next
            if cursor1.val >= cursor2.val:  # insert node-2 before node-1
                if prev: prev.next = cursor2
                cursor2.next = cursor1
                prev = cursor2
                cursor2 = temp2             # cursor2 move 1 step forward
            else:                           # move on
                if cursor1.next:            # cursor1 move 1 step forward
                    prev = cursor1
                    cursor1 = cursor1.next
                else:                       # cursor1 reached the end
                    cursor1.next = cursor2  # just connect the rest of list-2
                    cursor2 = None

        return head
