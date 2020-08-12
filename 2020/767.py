"""
767. Reorganize String

Given a string S, check if the letters can be rearranged so that
two characters that are adjacent to each other are not the same.

If possible, output any possible result.
If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # naive approach - create a dictionary and see if there's any char - x has count > n/2
        # if the answer exists: organise the string to proper output
        # analysis
        # phase 1: O(n)
        # phase 2: O(n)*2
        charDict = {}
        for c in S:
            if c not in charDict:
                charDict[c] = 1
            else:
                charDict[c] += 1
            if len(S) % 2:
                if charDict[c] > len(S)/2 + 1:
                    return ""
            else:
                if charDict[c] > len(S)/2:
                    return ""

        # validate twice: forward and backward
        tmp = self.organise([c for c in S])
        res = self.organise(tmp[::-1])

        return ''.join(res)

    def organise(self, res):
        for i in xrange(len(res)-1):
            j = i+1
            while res[i] == res[i+1] and j < len(res):
                if res[j] != res[i]:
                    res[i+1], res[j] = res[j], res[i+1]
                j += 1
        return res

# print Solution().reorganizeString('aab')
# print Solution().reorganizeString('aaab')
# print Solution().reorganizeString('aabb')
print Solution().reorganizeString("aaaaaaaabbccdef")
print Solution().reorganizeString("vvvlo")
print Solution().reorganizeString("baaba")
