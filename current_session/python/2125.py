from typing import List
import collections
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # check each row
        prevCnt = None
        ans = 0
        for row in bank:
            if "1" not in row: continue
            rowCnt = collections.Counter(row)
            currentCnt = rowCnt["1"]
            if prevCnt: ans += prevCnt*currentCnt
            prevCnt = currentCnt
        return ans