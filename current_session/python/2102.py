# can be done via SortedList()
# see more at https://leetcode.com/problems/sequentially-ordinal-rank-tracker/discuss/1623292/Python-SortedList-No-Need-to-Think-Explain-behind-the-scene!-O(logN)
# add: O(logN)
# get: O(logN)
# space: O(N)
import bisect
import collections
class SORTracker:

    def __init__(self):
        # maintain a sorted array
        # add: O(N)
        # get: O(logN)
        self.arr = []
        self.nameDict = collections.defaultdict(list)
        self.numOfGetCalled = 0

    def add(self, name: str, score: int) -> None:
        if not self.arr:
            self.arr.append(score)
            self.nameDict[score].append(name)
        else:
            bisect.insort_right(self.arr, score)
            bisect.insort_right(self.nameDict[score], name)

    def get(self) -> str:
        sc = self.arr[~self.numOfGetCalled]
        # find this score is which one
        # say we have 'seattle, 10', 'LA, 10', 'Vancouver, 10' => the numGetCalled is 2
        # we got: [10, 10, 10]
        # this 10 should represent Vancouver
        # we want to find out how many same scores at the right side of this one
        left = bisect.bisect_left(self.arr, sc)
        right = bisect.bisect_right(self.arr, sc)
        assert((right-left) == len(self.scoreDict[sc]))
        x = len(self.arr)-1-self.numOfGetCalled
        cnt = right-1-x
      
        self.numOfGetCalled += 1
        return self.nameDict[sc][cnt]


# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()