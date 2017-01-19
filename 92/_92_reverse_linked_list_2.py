"""
92. Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≦ m ≦ n ≦ length of list.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # e.g.      1   ->   2   ->   3   ->   4   ->   5   ->   6
        #           1        2   ->   3   ->   4   ->   5   ->   6
        #         prev    temp/tail  head
        #           1        2   <-   3        4   ->   5   ->   6
        #         prev     tail      temp     head
        if m == n: return head
        dummy, dummy.next = ListNode(0), head
        prev = dummy                                # prev is to connect nodes after m (temp)
        counter = 0
        while counter < n:
            counter += 1
            if counter < m:                         # go next spot
                prev, head = head, head.next
            elif counter == m:                      # setup temp and tail here
                temp = head
                prev.next, tail, head = None, head, head.next
                tail.next = None                    # tail is to connect nodes after n (head)
            elif counter > m and counter <= n:      # reverse this part
                temp, head.next, head = head, temp, head.next

        prev.next, tail.next = temp, head
        return dummy.next