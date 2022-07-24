# least recently used cache
# maintain a linked list and Dictionary

import collections
class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.cnt = 0
        self.head, self.tail = LinkedListNode(-1, -1), LinkedListNode(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def append(self, node):
        # append a new node at the end
        cur = self.tail.prev
        cur.next, node.prev = node, cur
        node.next, self.tail.prev = self.tail, node
        self.cnt += 1
        return
    
    def remove(self, cur):
        # remove the given node
        if self.cnt != 0:
            p, n = cur.prev, cur.next
            p.next, n.prev = n, p
            # return cur(?)
            self.cnt -= 1
        return cur

class LRUCache:

    def __init__(self, capacity: int):
        # least recent used -> .... -> most recent used
        self.cap = capacity
        self.linkedList = LinkedList()
        self.kDict = collections.defaultdict(LinkedListNode)

    def get(self, key: int) -> int:
        if key in self.kDict:
            node = self.linkedList.remove(self.kDict[key])
            self.linkedList.append(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        node = LinkedListNode(key, value)
        # if node in dict
        if key in self.kDict:
            x = self.linkedList.remove(self.kDict[key])
            del self.kDict[key]
        
        self.linkedList.append(node)
        self.kDict[key] = node
        
        # if the size is too big
        if self.linkedList.cnt > self.cap:
            lru = self.linkedList.head.next
            _ = self.linkedList.remove(lru)
            del self.kDict[lru.key]
        return
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

obj = LRUCache(2)
obj.put(2,1)
obj.put(2,2)
print(obj.get(2))