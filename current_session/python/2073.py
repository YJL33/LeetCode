from typing import List
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # simply simulate the process
        cnt = 0
        while tickets[k] != 0:
            tmp = []
            for t in tickets:
                if t != 0:
                    tmp.append(t-1)
                    cnt += 1
                    if len(tmp) >= k+1 and tmp[k] == 0: break
                else:
                    tmp.append(0)
            tickets = tmp
        return cnt
            