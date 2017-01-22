"""
147. Insertion Sort List

Sort a linked list using insertion sort.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # time complexity = O(n2)

        dummy_head = ListNode(0)    # always pointing at head of sorted singly-linked list
        dummy_head.next = head

        cursor = head               # current unsorted node
        pre = dummy_head            # position of incoming node in sorted singly-linked part

        # We're going to deal with the "cursor.next" Node
        while cursor and cursor.next:
            # cursor go next if already locally sorted
            if cursor.val < cursor.next.val:
                cursor = cursor.next
                continue

            # After following ops, pre will point at before the position of cursor should be at
            if pre.next.val > cursor.next.val:
                pre = dummy_head
            while pre.next.val < cursor.next.val:
                pre = pre.next

            # Insert "cursor.next" to here
            temp = cursor.next          # it's current position in un-sorted linklist
            cursor.next = temp.next     # the next node needs to check
            temp.next = pre.next        # insert here, link with the one should be its next ...
            pre.next = temp             # ... and the one should be its previous

        return dummy_head.next
