"""
86. Partition List

Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # seek through all linklist, if small => connect to 1st half, else => connect to 2nd half
        # analysis: n nodes => 3n + 6 (operations)

        newhead = ListNode(0)
        secondhalf = ListNode(0)

        first, second = newhead, secondhalf

        while head:
            if head.val < x:
                first.next = head
                first = head
            else:
                second.next = head
                second = head
            head = head.next

        # Here merge two part
        second.next = None      # this is important
        first.next = secondhalf.next
        return newhead.next




