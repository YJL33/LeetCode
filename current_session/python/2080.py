# construct a dictionary:
# key = given value
# value = index
# when receive a query, find its bisect left on the given index(key)
from typing import List
from collections import defaultdict
import bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freqDict = defaultdict(list)
        for i in range(len(arr)):
            a = arr[i]
            self.freqDict[a].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        # find the bisect index
        start = bisect.bisect_left(self.freqDict[value], left)
        end = bisect.bisect_right(self.freqDict[value], right)
        return end-start
       

# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)