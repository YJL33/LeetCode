"""
see https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        cd = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = []
        for d in digits:
            if len(ans) == 0:
                for c in cd[d]:
                    ans += c,
            else:
                tmp = []
                for a in ans:
                    for c in cd[d]:
                        tmp += a+c,
                ans = tmp

        return ans

print(Solution().letterCombinations('234'))
print(Solution().letterCombinations('2'))
print(Solution().letterCombinations(''))
