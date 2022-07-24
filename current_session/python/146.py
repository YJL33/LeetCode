"""
see https://leetcode.com/problems/lru-cache/
"""
import collections
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    # idea: linked-list + dictionary
    # dictionary: key = key, value = Node (in order to update the linked-list)
    # linked-list Node: key, value, prev, next

    # get: query dictionary, and update linked list
    # put: query dictionary, and update linked list (create/remove if needed)
    # time analysis: O(1) to update/add/remove hashMap (worst case O(N) if serious hash collision), O(1) for linkedlist insert/remove
    # space analysis: O(N) for both dictionary and linked-list
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = collections.defaultdict()
        self.root = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.root.next = self.tail
        self.tail.prev = self.root
        self.count = 0
    
    # check the dictionary to see if exist or not.
    # if exist, go to the node, keep the value, and update the linked-list, and then return the value at the end
    # time analysis: O(1) to query key-pair in dict, O(1) to remove/add node in linked-list
    def get(self, key: int) -> int:
        # requirement: avg time O(1)
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    # check the dictionary to see if exist or not.
    # if exist, go to the node, update the value, and update the linked-list
    # if not, then we have a new pair to add.
    # First check the size of linked-list. if reached the capacity remove lru then and add the new pair
    # time analysis: O(1) to query/removal key-pair in dict, O(1) to remove/add node in linked-list
    def put(self, key: int, value: int) -> None:
        # requirement: avg time O(1)
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self._remove(node)
            self._add(node)
            return
        else:
            if self.count == self.capacity:
                node = self.root.next
                del self.dict[node.key]
                self._remove(node)
            else:
                self.count += 1

            new_node = Node(key, value)
            self.dict[key] = new_node
            self._add(new_node)
            return
    
    # remove the given node from linked-list (node itself could still be useful)
    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p
        node.prev, node.next = None, None
        return
    
    # add a node at the tail of linked-list.
    def _add(self, node):
        p, n = self.tail.prev, self.tail
        p.next = node
        n.prev = node
        node.prev, node.next = p, n
        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)