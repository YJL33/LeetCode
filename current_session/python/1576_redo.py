class Solution:
    def modifyString(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i] == "?":
                nbs = set()
                if res: nbs.add(res[-1])
                if i+1 < len(s): nbs.add(s[i+1])
                for c in "abc":
                    if c not in nbs:
                        res.append(c)
                        break
            else:
                res.append(s[i])
        # print(s)

        return ''.join(res)

print(Solution().modifyString("?zs"))
print(Solution().modifyString("ubv?w"))
print(Solution().modifyString("j?qg??b"))
print(Solution().modifyString("??yw?ipkj?"))