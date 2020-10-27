"""
see https://leetcode.com/problems/find-and-replace-in-string/
"""
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        res = [c for c in S]

        for i in range(len(indexes)):
            l, r = indexes[i], indexes[i]+len(sources[i])
            if S[l:r] == sources[i]:            # found it!
                res[l] = targets[i]
                for j in range(l+1, r):
                    res[j] = ''

        return ''.join(res)

print(Solution().findReplaceString(S = "abcd", indexes = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]), 'should be eeebffff')
print(Solution().findReplaceString(S = "abcd", indexes = [0, 2], sources = ["ab","ec"], targets = ["eee","ffff"]), 'should be eeecd')