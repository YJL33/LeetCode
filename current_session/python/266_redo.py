# use a Counter
import collections
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cd = collections.defaultdict(int)
        for i in range(len(s)):
            cd[s[i]] += 1
        
        hasOdd = False
        for k, v in cd.items():
            if v%2:
                if not hasOdd:
                    hasOdd = True
                else:
                    return False
        return True

print(Solution().canPermutePalindrome("cccaaa"))
# print(Solution().canPermutePalindrome("aab"))
# print(Solution().canPermutePalindrome("carerac"))