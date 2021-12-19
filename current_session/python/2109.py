from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        if not spaces: return s
        end = spaces[0]
        res = [s[:end]]
        start = spaces[0]
        spaces.append(len(s))
        for end in spaces[1:]:
            x = s[start:end]
            x[0].upper()
            res.append(x)
            start = end
        return " ".join(res)
