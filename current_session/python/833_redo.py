
from typing import List
class Solution:
    def findReplaceString_sort(self, s:str, indices:List[int], sources:List[str], targets:List[str]) -> str:
        # find out need to action or not
        toReplace = []
        for i in range(len(sources)):
            subStr = sources[i]
            j = indices[i]
            if subStr == s[j:j+len(subStr)]:
                toReplace.append((indices[i], i))
        
        toReplace.sort()            # O(nlogn)
        # print('to replace:', toReplace)
        # replace here
        # offset only work on string itself
        offset = 0
        for i, j in toReplace:
            start, source, target = i, sources[j], targets[j]
            end = start+len(source)
            s = s[:start+offset] + target + s[end+offset:]
            offset = offset + len(target) - len(source)

        return s
    
    def findReplaceString_linear(self, s:str, indices:List[int], sources:List[str], targets:List[str]) -> str:

        res = [c for c in s]

        for i in range(len(indices)):
            l, r = indices[i], indices[i]+len(sources[i])
            if s[l:r] == sources[i]:
                res[l] = targets[i]
                for j in range(l+1, r):
                    res[j] = ""
        
        return "".join(res)



# print(Solution().findReplaceString(s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]))
# print(Solution().findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))
print(Solution().findReplaceString_linear("vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"]))
