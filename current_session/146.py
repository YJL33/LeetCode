"""
see https://leetcode.com/problems/lru-cache/
"""
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # store key and value in both dict and doubly linked list
        self.size = capacity
        self.dict = {}

        # all values are stored between head and tail
        # head and tail are simply dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict.keys():
            n = self.dict[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict.keys():
            self._remove(self.dict[key])
        recent = Node(key, value)
        self._add(recent)
        self.dict[key] = recent
        if len(self.dict.keys()) > self.size:
            least = self.head.next
            self._remove(least)
            del self.dict[least.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)