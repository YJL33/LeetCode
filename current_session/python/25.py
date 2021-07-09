"""
25. Reverse Nodes in k-Group

Given a linked list,
reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        if k == 1:
            return head

        # use dummy head to save "previous part"
        # go forward k steps, and save the "next part"
        # reverse the LL
        # hook 3 parts: prev -> reversed LL -> next
        # continue

        dummyHead = ListNode(0)
        prev, nxt = dummyHead, head

        while nxt != None and nxt.next != None:
            tail = self.goKStepsToFindTail(nxt, k)
            
            if tail == False:
                break

            newHead = self.reverseLL(nxt, tail)
            newTail = self.goKStepsToFindTail(newHead, k)

            prev.next = newHead
            nxt = newTail
            prev = self.goKStepsToFindTail(newHead, k-1)

        return dummyHead.next


    def goKStepsToFindTail(self, head, k):
        # return tail
        steps = 0
        while steps < k and head != None:
            head = head.next
            steps += 1
        # print "go K steps, now at: ", head.val
        if steps == k:
            return head
        else:
            return False

    def reverseLL(self, head, tail):
        # print "given: ", head.val, tail.val
        dh = ListNode(0)
        dh.next = head

        prev, cursor = tail, head

        while cursor != tail:
            nxt = cursor.next
            # print "reversing: ", prev.val, cursor.val, nxt.val
            cursor.next = prev
            # print "keep reversing...", cursor.val, cursor.next.val
            prev = cursor
            cursor = nxt

        # print "reversed head: ", prev.val
        # print "reversed result: ", prev.val, prev.next.val
        return prev

A = ListNode(1)
B = ListNode(2)
C = ListNode(3)
D = ListNode(4)
E = ListNode(5)

A.next = B
B.next = C
C.next = D
D.next = E
E.next = None


res, resList = Solution().reverseKGroup(A, 3), []
while res != None:
    resList += res.val,
    res = res.next

print resList