# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head: return 0
        ans = 0
        node = head
        while node:
            ans *= 2
            ans += node.val
            node = node.next

        return ans

def getListNode(arr):
    dh = ListNode(0)
    cur = dh
    for a in arr:
        tmp = ListNode(a)
        cur.next = tmp
        cur = tmp
    return dh.next


print(Solution().getDecimalValue(getListNode([1,0,1])))
print(Solution().getDecimalValue(getListNode([0])))
print(Solution().getDecimalValue(getListNode([1])))
print(Solution().getDecimalValue(getListNode([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0])))
print(Solution().getDecimalValue(getListNode([0,0])))