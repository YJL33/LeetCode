"""
1153
"""
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        l1, l2 = len(set(str1)), len(set(str2))
        if l1 < l2:
            return False
        if l1 == l2 == 26:
            return (str1 == str2)
        
        mp = {}     # map of a-z
        for i in range(len(str1)):
            a, b = str1[i], str2[i]
            if a not in mp:
                mp[a] = b
            elif mp[a] != b:
                return False
        return True

print(Solution().canConvert("abcdefghijklmnopqrstuvwxyz","bcadefghijklmnopqrstuvwxzz"), 'should be True')