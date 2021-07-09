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
        res = []
        for n in digits:
            if not res:
                for c in cd[n]:
                    res += c,
            else:
                tmp = []
                for r in res:
                    for c in cd[n]:
                        tmp += [r+c]
                res = tmp

        return res

print(Solution().letterCombinations('234'))
print(Solution().letterCombinations('2'))
print(Solution().letterCombinations(''))
