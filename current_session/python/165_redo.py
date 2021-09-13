
# simply parse
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        L = max(len(v1), len(v2))
        for i in range(L):
            a = int(v1[i]) if i < len(v1) else 0
            b = int(v2[i]) if i < len(v2) else 0
            if a > b: return 1
            elif a < b: return -1
        return 0


print(Solution().compareVersion(version1 = "1.01", version2 = "1.001"))
print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0"))
print(Solution().compareVersion(version1 = "0.1", version2 = "1.1"))
print(Solution().compareVersion("1.0.1", "1"))
print(Solution().compareVersion("7.4.2.4", "7.5.3"))