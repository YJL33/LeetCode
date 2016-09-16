"""
146. LRU Cache

    Total Accepted: 87010
    Total Submissions: 548720
    Difficulty: Hard

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and set.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache,
           otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present.
                When the cache reached its capacity,
                it should invalidate the least recently used item before inserting a new item.
"""
from collections import OrderedDict
class LRUCache(object):
    # Use OrderedDict: 208ms
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return -1        

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            del self.cache[key]     # Remove old entry to maintain the FIFO
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(False)   # Arg: True: FILO, False: FIFO
