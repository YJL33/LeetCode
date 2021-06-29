"""
1576
"""
class Solution:
    def modifyString(self, s: str) -> str:
        if len(s) == 0: return
        if len(s) == 1: return 'a' if s == '?' else s
        res = []
        cand = set(['a', 'b', 'c'])
        for i in range(len(s)):
            nbs = set()      # prev, next
            if res: nbs.add(res[-1])
            if i < len(s)-1: nbs.add(s[i+1])
            c = s[i]
            if c != '?':
                res += c,
            else:
                xor = cand.difference(nbs)
                print(xor)
                res += xor.pop(),
        return ''.join(res)

print(Solution().modifyString("?zs"))
print(Solution().modifyString("ubv?w"))
print(Solution().modifyString("j?qg??b"))
print(Solution().modifyString("??yw?ipkj?"))
