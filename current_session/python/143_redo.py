# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def show(self):
        print(self.val)
        if self.next: self.next.show()

# reverse the 2nd half and merge them (zig-zag)

from typing import Optional
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        prev, slow, fast = None, head, head

        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        
        if not prev: return head

        # reverse 2nd helf
        def reverse(root):
            node, nxt = root, root.next
            node.next = None

            while node and nxt:
                tmp = nxt.next
                nxt.next, node = node, nxt
                nxt = tmp
            return node

        # cut linklist and reverse 2nd half
        prev.next = None
        x = reverse(slow)

        dummyHead = ListNode(0)
        cur = dummyHead
        while head or x:
            if head: cur.next, cur, head = head, head, head.next
            if x: cur.next, cur, x = x, x, x.next

        return dummyHead.next

e = ListNode(5)
d = ListNode(4)
c = ListNode(3,d)
b = ListNode(2,c)
a = ListNode(1,b)
print(Solution().reorderList(a))
print(Solution().reorderList(e))