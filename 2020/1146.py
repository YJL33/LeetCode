"""
see https://leetcode.com/problems/snapshot-array/
"""
class SnapshotArray(object):

    def __init__(self, l):
        """
        :type length: int
        """
        self.ver = {}
        for i in range(l):
            self.ver[i] = {0:0}
        self.snapCnt = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.ver[index][self.snapCnt] = val

    def snap(self):
        """
        :rtype: int
        """
        self.snapCnt += 1
        return self.snapCnt-1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # find the value of the maximum snapcnt < snap_id
        ls = self.ver[index]
        return self.finder(ls, snap_id)

    def finder(self, d, tgt):
        # print(d, tgt)
        keys = d.keys()
        l, m, r = 0, 0, len(keys)
        keys.sort()
        while l < r:
            m = (r+l)/2
            if keys[m] > tgt:        # m is too big
                r = m
            else:
                l = m+1
        return d[keys[l-1]]
        

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)