# need random module
# to make insert and remove O(1), we simply use a set
# to make random O(1), we maintain a dict that has key: insert order, value: val
# so that we can use random to decide a 'index' and remove it
# after removal we back-fill the last element to the removed empty spot

# Ideal solution: use random.choice( list(dict.items()) )

import random
class RandomizedSet:
    def __init__(self):
        self.nodeSet = set()
        self.rndDict = {}
        self.indexDict = {}

    def insert(self, val: int) -> bool: 
        if val in self.nodeSet: return False
        self.nodeSet.add(val)
        i = len(self.rndDict)
        self.rndDict[i] = val
        self.indexDict[val] = i
        return True

    def remove(self, val: int) -> bool:
        if val not in self.nodeSet: return False
        self.nodeSet.remove(val)
        i = self.indexDict[val]
        lastI = len(self.indexDict)-1
        lastVal = self.rndDict[lastI]
        # back-fill
        self.indexDict[lastVal] = i
        self.rndDict[i] = lastVal
        # remove
        del self.rndDict[lastI]
        del self.indexDict[val]
        return True

    # make sure the possibility is the same
    # say we have N elements, pick index from 0 to N-1
    def getRandom(self) -> int:
        x = random.random()
        i = int(x * len(self.nodeSet))
        return self.rndDict[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()