from typing import List
class Solution:
    def findReplaceString(self, s:str, indices:List[int], sources:List[str], targets:List[str]) -> str:
        # tail everything together
        inp = [(indices[i], sources[i], targets[i]) for i in range(len(indices))]
        inp.sort()
        return self.helper(s, inp)

    def helper(self, s:str, inp: List[tuple], offset=0) -> str:
        # validate whether need action or not first
        # if needed: add into stack
        # can be done with recursion
        # need to handle offset
        # print("s:", s, "indices:", indices, "offset:", offset)

        if not inp: return s
        start = inp[0][0]+offset
        end = min(start+len(inp[0][1]), len(s))
        prefix = s[:start]

        if s[start:end] == inp[0][1]:
            offset += len(inp[0][2])-len(inp[0][1])
            return self.helper(prefix+inp[0][2]+s[end:], inp[1:], offset)
        else:
            return self.helper(s, inp[1:], offset)

print(Solution().findReplaceString(s = "abcdefghijklm", indices = [0, 2, 4, 6, 8], sources = ["a", "c", "e", "g", "i"], targets = ["xxx", "xxx", "xxx", "", "xxx"]))
print(Solution().findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]))
print(Solution().findReplaceString("vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"]))
