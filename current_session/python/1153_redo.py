# simply use 2 Pointers
# use a map/dict: key=str1 char, val=str2 char
# if char in pointer1 not in dict: dict[char1] = char2
# else: verify whether dict[char1] == char2

class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        l1, l2 = len(set(str1)), len(set(str2))
        if l1 < l2: return False
        elif l1 == 26 == l2: return (str1 == str2)

        charDict = {}
        for i in range(len(str1)):
            c1, c2 = str1[i], str2[i]
            if c1 not in charDict:
                charDict[c1] = c2
            elif charDict[c1] != c2:
                return False
        return True

print(Solution().canConvert("aabcc", "ccdee"))
print(Solution().canConvert("leetcode", "codeleet"))    # false
print(Solution().canConvert("abcde", "eeeee"))
print(Solution().canConvert("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"))    # false