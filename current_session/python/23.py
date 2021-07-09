"""
23. Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
Accepted 620,826
Submissions 1,575,165
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    # recursive
    # split them to half
    # singly-linked list -> create new nodes

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) <= 1:
            return lists[0]

        mid = len(lists)//2     # floor division
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])

        dummyHead = ListNode(0)
        current = dummyHead

        while left != None or right != None:
            if right == None or (left != None and left.val <= right.val):
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        return dummyHead.next

