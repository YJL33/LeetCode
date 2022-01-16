from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        tmp = ""
        for c in s:
            if len(tmp) < k:
                tmp += c
            if len(tmp) == k:
                res.append(tmp)
                tmp = ""
        if tmp:
            while len(tmp) < k:
                tmp += fill
            res.append(tmp)
        return res
            