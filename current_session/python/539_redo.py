from typing import List
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # convert to min and use absolute diff (x, 360-x)
        timeSet = set()

        def convert(tp):
            HH, MM = tp.split(":")
            return int(HH)*60+int(MM)

        # convert all of those
        for tp in timePoints:
            t = convert(tp)
            if t in timeSet:
                return 0
            else:
                timeSet.add(t)
        
        A = [t for t in timeSet]
        A.sort()
        minDiff = 60*24+A[0]-A[-1]
        prev = A[0]
        for i in range(1,len(A)):
            minDiff = min(minDiff, A[i] - prev)
            prev = A[i]
        
        return minDiff
