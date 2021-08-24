# keep increase time (+1 min) until it meets criteria
class Solution:
    def nextClosestTime(self, time:str) -> str:
        HH, MM = time.split(":")
        self.digitSet = set([H for H in HH] + [M for M in MM])
        h, m = int(HH), int(MM)
        while True:
            h, m = self._addOneMin(h, m)
            if self._isValid(h, m): return self._isValid(h, m)
    
    def _addOneMin(self, h, m):
        m += 1
        if m == 60: h, m = h+1, 0
        if h == 24: h = 0
        return h, m
    
    def _isValid(self, h, m):
        newHH, newMM = str(h), str(m)
        if len(newHH) == 1: newHH = "0"+newHH
        if len(newMM) == 1: newMM = "0"+newMM
        newSet = set([H for H in newHH] + [M for M in newMM])
        if any([x not in self.digitSet for x in newSet]): return False
        return newHH+":"+newMM

print(Solution().nextClosestTime("19:34"))
print(Solution().nextClosestTime("23:59"))