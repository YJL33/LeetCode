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
    def sorter(self, node, prev, width, getN=False):
        # according to the width, mergesort two sorted sublists. (h1 to t1, h2 to t2)
        cursor = prev
        h1, t1, h2, t2, nexthead, counter = self.parser(node, width)
        if getN: sublen = counter

        if t1: t1.next = None
        if t2: t2.next = None
        #print "counter: ", counter
        
        while counter:                              # counter = length of merged sublist
            counter -= 1
            if not h1:
                cursor.next = h2
                while h2.next: h2 = h2.next
                cursor, counter = h2, 0
            elif not h2:
                cursor.next = h1
                while h1.next: h1 = h1.next
                cursor, counter = h1, 0
            elif h1.val > h2.val:
                cursor.next, cursor, h2 = h2, h2, h2.next
            else:
                cursor.next, cursor, h1 = h1, h1, h1.next

        cursor.next = nexthead
        if getN: return nexthead, cursor, sublen
        return nexthead, cursor                             # return the next pos
    
    def parser(self, node, width):
        # get h1, t1, h2, t2, nexthead, and counter
        counter = 0
        h1 = node
        t1 = h2 = t2 = None
        for i in xrange(2*width):
            if not node: break
            if counter == (width-1): t1 = node
            if counter == width: h2 = node
            if counter == (2*width-1): t2 = node
            node = node.next
            counter += 1

        return h1, t1, h2, t2, node, counter

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy, dummy.next, cursor = ListNode(0), head, head
        
        n = 2                                           # n is at least 2
        getN = True
        width = 1                                       # width of sublists

        while width < n:
            prev = dummy
            if getN:
                n = 0
                while head:
                    head, prev, s = self.sorter(head, prev, width, getN)
                    n += s
                getN = False
            else:        
                while head:
                    head, prev = self.sorter(head, prev, width)
            head = dummy.next
            """
            while head:
                print head.val                          # show current linklist
                head = head.next
            head = dummy.next
            """
            width *= 2

        return dummy.next
        # T: O(nlogn) but slower than recursion version
        # record next layer's node should be faster, but break the Space: O(1) rule