"""
387
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cd = {}
        seen = set()
        for i, c in enumerate(s):
            if c not in seen:
                cd[c] = i
                seen.add(c)
            elif c in cd:
                del cd[c]
        return min(cd.values()) if cd else -1

print(Solution().firstUniqChar("acaadcad"))
print(Solution().firstUniqChar("aadadaad"))