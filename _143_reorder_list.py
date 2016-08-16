"""
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        # construct a forward and reverse list, finally connect them together
        # note that forward list must be longer or equal to reverse list
        if not head: return head

        dummy, dummy.next = ListNode(0), head
        fast = slow = head
        tail = None

        while fast and fast.next:                           # not reach the end yet
            tail, slow, fast = slow, slow.next, fast.next.next
        tail, slow = slow, slow.next                        # move one step more
        # after this line, it become 2 parts, beginning with slow and dummy.next

        # reverse 2nd part
        rev = None
        while slow:
            rev, rev.next, slow = slow, rev, slow.next
        if tail: tail.next = None                           # cut off the 1st part and 2nd part

        # now splice them together: beginning with rev and dummy.next
        toward = dummy.next
        while toward and rev:
            temp = toward.next
            toward.next = rev
            rev = rev.next
            toward.next.next = temp
            toward = temp