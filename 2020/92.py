# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head

        prev, p1, i = dummyHead, dummyHead, 0
        while i != m:
            prev, p1, i = p1, p1.next, i+1

        p2, j = p1, i
        while j != n:
            p2, j = p2.next, j+1
        tail = p2.next
        # print(prev.val, p1.val, p2.val, tail.val)

        # reverse here
        while i != j:
            nxt = p1.next
            p1.next = tail
            tail, p1, i = p1, nxt, i+1
        
        # finalize
        p1.next = tail
        prev.next = p1

        return dummyHead.next
