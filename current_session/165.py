"""
https://leetcode.com/problems/compare-version-numbers/
"""
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = [int(x) for x in version1.split(".")], [int(x) for x in version2.split(".")]
        p1, p2 = 0, 0

        # compare versions dot by dot
        while p1 < len(v1) and p2 < len(v2):
            a, b = v1[p1], v2[p2]
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                p1, p2 = p1+1, p2+1

        # if number of layers (dots) are not the same
        # even if there's a layer, we wanna check whether the sum is 0 or not
        tmp1, tmp2 = sum(v1[p1:]), sum(v2[p2:])

        # compare the accumulated layers
        if tmp1 > tmp2:
            return 1
        elif tmp1 < tmp2:
            return -1
        else:
            return 0

print(Solution().compareVersion(version1 = "1.01", version2 = "1.001"), '0')
print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0"), '0')
print(Solution().compareVersion(version1 = "0.1", version2 = "1.1"), '-1')
print(Solution().compareVersion(version1 = "1.0.1", version2 = "1"), '1')
print(Solution().compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"), '-1')
