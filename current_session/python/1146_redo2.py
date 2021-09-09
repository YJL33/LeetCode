import collections
import bisect

class SnapshotArray:

    def __init__(self, L: int):
        self.snapShotId = 0
        self.sIdDict = collections.defaultdict(list)      # key: index, value: (snapShot, value)
        self.valDict = collections.defaultdict(list)      # key: index, value: (snapShot, value)
        for i in range(L):
            self.sIdDict[i].append(self.snapShotId)
            self.valDict[i].append(0)
        return

    def set(self, index: int, val: int) -> None:
        # update the list if exist
        if self.sIdDict[index][-1] == self.snapShotId:
            self.valDict[index][-1] = val
        else:
            self.sIdDict[index].append(self.snapShotId)
            self.valDict[index].append(val)
        return

    def snap(self) -> int:
        self.snapShotId += 1
        return self.snapShotId-1

    def get(self, index: int, snap_id: int) -> int:
        j = bisect.bisect_right(self.sIdDict[index], snap_id)
        return self.valDict[index][j-1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)