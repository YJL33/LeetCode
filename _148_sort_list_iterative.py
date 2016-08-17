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
    # mergesort => mergesort the 2nd half => merge together
    def sorter(self, node, prev, width):
        # according to the width, sort two sublists.
        cursor = prev
        h1 = node
        t1, c1 = self.goNext(node, width-1, True)
        h2 = self.goNext(node, width)
        t2, c2 = self.goNext(node, width*2-1, True)
        tail, c3 = self.goNext(node, width*2, True)
        #print h1.val, t1.val, h2.val, t2.val
        if t1: t1.next = None
        if t2: t2.next = None
        counter = max(c1, c2, c3)
        #print "counter: ", counter
        
        while h1 and h2 or counter:
            #print "sorting...", h1.val, h2.val
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
        #print "n: ", n
        counter = 0
        while n > counter and node:
            counter += 1 
            node = node.next

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