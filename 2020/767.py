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
import heapq

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
        # phase 2: O(n)+O(xlog(x)), where x = number of unique characters
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

        tmp = self.organize(charDict, len(S))

        return ''.join(tmp)

    def organize(self, cd, n):
        hp = []
        for k in cd.keys():
            heapq.heappush(hp, ((-1)*cd[k], k))
        res = [0 for _ in range(n)]
        cnt, char = heapq.heappop(hp)
        index = [i for i in range(0, n, 2)] + [j for j in range(1, n, 2)]
        for i in index:
            # print char, cnt
            if cnt < 0:
                res[i] = char
                cnt += 1
            else:
                cnt, char = heapq.heappop(hp)
                res[i] = char
                cnt += 1
        return res

# print Solution().reorganizeString('aab')
# print Solution().reorganizeString('aaab')
# print Solution().reorganizeString('aabb')
print Solution().reorganizeString("aaaaaaaabbccdef")
print Solution().reorganizeString("vvvlo")
print Solution().reorganizeString("baaba")
