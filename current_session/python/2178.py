from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum%2: return []

        ans = []
        i = 2
        while finalSum >= i:
            ans.append(i)
            finalSum -= i
            i += 2
        
        ans[-1] += finalSum
        return ans