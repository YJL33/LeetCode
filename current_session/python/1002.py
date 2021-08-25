from typing import List
import collections
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = collections.Counter(words[0])
        for w in words[1:]:
            res = res & collections.Counter(w)
        return [r for r in res.elements()]

print(Solution().commonChars(["bella","label","roller"]))
print(Solution().commonChars(["cool","lock","cook"]))