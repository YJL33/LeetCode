"""
146
"""
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        # create a dict and a doubly linked list
        self.size = capacity
        self.nd = {}                # key: key, value: node
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nd:
            node = self.nd[key]
            self._rmvFmLL(node)
            self._addToLL(node)
            return node.v
        else:
            return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.nd:
            self._rmvFmLL(self.nd[key])
        n = Node(key, value)
        self._addToLL(n)
        self.nd[key] = n
        if len(self.nd.keys()) > self.size:
            least = self.head.next
            self._rmvFmLL(least)
            del self.nd[least.k]
        
    def _addToLL(self, node):
        x = self.tail.prev
        x.next = node
        node.prev = x
        self.tail.prev = node
        node.next = self.tail

    def _rmvFmLL(self, node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)