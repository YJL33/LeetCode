'''
234
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # O(n) time and O(1) space?
        # use next : next.next
        if not head: return True
        if not head.next: return True
        if not head.next.next: return head.next.val == head.val

        prev, c1, c2 = head, head.next, head.next.next
        prev.next = None
        # find the middle point while reversing first half
        while c1.next and c2.next and c2.next.next:
            tmp = c1
            c1, c2 = c1.next, c2.next.next
            prev, tmp.next = tmp, prev
        
        # handle if length of ListNode is odd
        if c2.next is None:
            # check from head
            return self.checker(prev, c1.next)
        else:
            r = c1.next
            c1.next = prev
            return self.checker(c1, r)
    
    def checker(self, n1: ListNode, n2: ListNode) -> bool:
        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1, n2 = n1.next, n2.next
        if not n1 and not n2:
            return True
        else:
            return False
            