from sortedcontainers import SortedList
class Node:
    def __init__(self,key,val,freq=1,time=0):
        self.key = key
        self.val = val
        self.freq = freq
        self.time = time

# sortedlist
class LFUCache:
    def __init__(self, capacity: int):
        self.sl = SortedList(key=lambda x:(-x.freq,-x.time))
        self.nd = {}                  # key: node
        self.cap = capacity
        self.time = 0
    
    def _add(self, node):
        self.sl.add(node)
        self.nd[node.key] = node
        
    def _remove(self, node):
        del self.nd[node.key]
        self.sl.remove(node)
        
    def get(self, key: int) -> int:
        if key not in self.nd: return -1
            
        node = self.nd[key]
        self._remove(node)
        node.freq += 1
        node.time = self.time

        self._add(node)
        self.time += 1
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap == 0: return

        freq = 1
        if key in self.nd:
            freq += self.nd[key].freq
            self._remove(self.nd[key])
        elif len(self.nd) >= self.cap:
            self._remove(self.sl[-1])
        node = Node(key,value,freq,self.time)

        self._add(node)
        self.time += 1
        return
