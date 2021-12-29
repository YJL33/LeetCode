# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # identify the even groups and reverse it
        dh = ListNode(0)
        dh.next = head
        cur = dh
        gl = 1
        
        def check(lastGroup, L):
            # if count is even: reverse
            cnt = 0
            node = lastGroup
            while node and node.next and cnt < L:
                node = node.next
                cnt += 1
            if cnt%2:           # don't reverse
                # print('no rev', node.val if node else 'x', 'cnt=', cnt)
                return node, node.next if node else None     # return the tail
            else:               # reverse
                # node could be None
                # lastGroup.next could be None
                if not lastGroup.next: return None, None
                cur = lastGroup.next
                last = lastGroup.next
                ll = node.next if node else None
                prev = None
                while cur and cur != ll:
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp
                lastGroup.next = prev
                last.next = ll
                # print('do rev:', last.val if last else 'x', ll.val if ll else 'x')
                return last, ll
            
        while cur:
            cur, _ = check(cur, gl)
            gl += 1
        
        return dh.next
                