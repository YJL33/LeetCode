"""
148. Sort List

Sort a linked list in O(n log n) time using constant space complexity.
"""
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    # implement mergesort (iterative):
    # mergesort sublist length = 1 => 2 => 4 => 8 ....
    def sorter(self, node, prev, width):
        # according to the width, sort two sublists.
        cursor = prev
        h1 = node
        t1 = self.goNext(node, width-1)
        h2 = self.goNext(node, width)
        t2 = self.goNext(node, width*2-1)
        tail, counter = self.goNext(node, width*2, True)

        if t1: t1.next = None
        if t2: t2.next = None
        #print "counter: ", counter
        
        while h1 and h2 or counter:
            counter -= 1
            if not h1:
                cursor.next, cursor, h2 = h2, h2, h2.next
            elif not h2:
                cursor.next, cursor, h1 = h1, h1, h1.next
            elif h1.val > h2.val:
                cursor.next, cursor, h2 = h2, h2, h2.next
            else:
                cursor.next, cursor, h1 = h1, h1, h1.next

        cursor.next = tail
        return tail, cursor                        # return the next pos
    

    def goNext(self, node, n, getLen=False):
        # go next for n steps, if meet None => return None.
        counter = 0
        for i in xrange(n):
            if not node: break
            node = node.next
            counter += 1

        if getLen:
            if counter != n: return None, counter
            return node, counter
        else:
            if counter != n: return None
            return node

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy, dummy.next, cursor = ListNode(0), head, head

        n = 0                                           # totally n nodes
        while cursor:
            n += 1
            cursor = cursor.next
        
        width = 1                                       # width of sublists
        while width < n:
            prev = dummy
            while head:
                head, prev = self.sorter(head, prev, width)
            head = dummy.next
            """
            while head:
                print head.val                          # show the current linklist
                head = head.next
            head = dummy.next
            """
            width *= 2
            #print "width: ", width

        return dummy.next
        # T: O(nlogn) but slower than recursion version
        # record next layer's node should be faster, but break the Space: O(1) rule