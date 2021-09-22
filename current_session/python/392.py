# use 2 pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(s)):
            while j < len(t) and t[j] != s[i]:
                j += 1
            # either j==len(t) or t[j] == s[i]
            if j == len(t):
                return False
            # move to next t
            else:
                j += 1

        return True

print(Solution().isSubsequence("abc", "ahbgdc"))
print(Solution().isSubsequence("axc", "ahbgdc"))