# use 2 pointers and span = n
from typing import Optional
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n:int) -> Optional[ListNode]:
        l, r = head, head
        dummyHead = ListNode(0)
        prev, dummyHead.next = dummyHead, head
        steps = 0
        while steps < n:
            r = r.next
            steps += 1
        while r != None:
            prev, l, r = l, l.next, r.next
        
        prev.next = l.next

        return dummyHead.next

e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)
bb = ListNode(2)
aa = ListNode(1, bb)
x = Solution().removeNthFromEnd(a, 2)
y = Solution().removeNthFromEnd(aa, 1)
while x:
    print(x.val)
    x = x.next
while y:
    print(y.val)
    y = y.next
