"""
1086
"""
from typing import List
import bisect
import math
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        score = {}
        for id, pt in items:
            if id not in score:
                score[id] = [-pt]
            else:
                bisect.insort_right(score[id], -pt)
                if len(score[id]) > 5:
                    score[id].pop()
                # score[id] += pt,
        res = []
        for k, v in score.items():
            res += [k, math.floor(-1*sum(v)/5.0)],
        
        res.sort()
        return res

print(Solution().highFive([[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]))        
print(Solution().highFive([[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]))