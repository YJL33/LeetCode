"""
382. Linked List Random Node

Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly.
Each element should have equal probability of returning.
solution.getRandom();
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution(object):
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.dummy, self.dummy.next = ListNode(0), head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        counter = 0
        if not self.dummy.next:
            return None

        cur = self.dummy.next
        while cur:
            cur = cur.next
            counter += 1

        pick, cur = random.randint(1,counter), self.dummy
        while pick:
            cur, pick = cur.next, pick-1

        return cur.val

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()