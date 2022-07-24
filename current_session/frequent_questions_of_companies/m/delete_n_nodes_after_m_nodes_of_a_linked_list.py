# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        aliveCnt, removeCnt = 1, 0
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead.next
        prev = None
        while cur:
            if aliveCnt < m:
                cur = cur.next
                aliveCnt += 1
            elif aliveCnt == m and removeCnt == 0:
                prev = cur
                cur = cur.next
                removeCnt += 1
            elif aliveCnt == m and removeCnt < n:
                cur = cur.next
                removeCnt += 1
            elif aliveCnt == m and removeCnt == n:
                cur = cur.next
                prev.next = cur
                prev = None
                aliveCnt, removeCnt = 1, 0
        
        if prev: prev.next = None
        
        return dummyHead.next

