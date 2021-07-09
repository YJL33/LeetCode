"""
708
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        ins = Node(insertVal)
        if not head:
            ins.next = ins
            return ins
        if head.next == head:
            head.next = ins
            ins.next = head
            return head
        
        p, c = None, head
        minN, maxN = None, None
        while c.next != head:
            # update min/max
            if not minN or c.val <= minN.val: minN = c
            if not maxN or c.val >= maxN.val: maxN = c
            # insert if available
            if p is not None and p.val <= insertVal <= c.val:
                p.next, ins.next = ins, p.next
                return head
            p, c = c, c.next
        
        # check once more
        if p is not None and p.val <= insertVal <= c.val:
            p.next, ins.next = ins, p.next
            return head
        if not minN or c.val <= minN.val: minN = c
        if not maxN or c.val >= maxN.val: maxN = c
        
        # print('min, max',minN.val, maxN.val)
        
        if minN.val <= insertVal <= maxN.val:
            c.next, ins.next = ins, c.next
        else:
            maxN.next, ins.next = ins, maxN.next
        
        return head