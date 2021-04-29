"""
93
"""
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # use dfs
        self.ans = []

        def isValid(s):
            # is it a good int?
            if len(s) > 1 and s[0] == '0':
                return False
            # convert to int
            if len(s) <= 3 and 0 <= int(s) <= 255:
                return True
            else:
                return False

        def dfs(s, prev):
            # print('now:', s, prev)
            if not s or len(prev) > 3:
                return
            elif isValid(s) and len(prev) == 3:
                prev += s,
                self.ans += ".".join(prev),
                return
            else:
                if isValid(s[0]):
                    dfs(s[1:], prev+[s[0]])
                if isValid(s[:2]):
                    dfs(s[2:], prev+[s[:2]])
                if isValid(s[:3]):
                    dfs(s[3:], prev+[s[:3]])

        dfs(s, [])

        return self.ans

print(Solution().restoreIpAddresses("25525511135"))
print(Solution().restoreIpAddresses("0000"))
print(Solution().restoreIpAddresses("1111"))
print(Solution().restoreIpAddresses("010010"))
print(Solution().restoreIpAddresses("101023"))