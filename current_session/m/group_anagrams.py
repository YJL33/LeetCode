from typing import List
import collections
class Solution:
    def groupAnagrams(self, A: List[str]) -> List[List[str]]:
        wd = collections.defaultdict(list)
        for i in range(len(A)):
            x = ''.join(sorted([c for c in A[i]]))
            wd[x].append(A[i])

        return wd.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))