'''
356
'''
import collections
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # for each y, calculate the avg x
        pd = collections.defaultdict(set)     # key = y, value = x
        for p in points:
            pd[p[1]].add(p[0])
        prevX = None
        for k, v in pd.items():
            avgX = sum(v)/(1.0*len(v))
            if prevX is not None and avgX != prevX: return False
            xs = [vs for vs in v]
            xs.sort()
            l, r = 0, len(xs)-1
            while l<r:
                if avgX-xs[l] != xs[r]-avgX: return False
                l, r = l+1, r-1
            prevX = avgX
        return True