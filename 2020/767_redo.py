"""
767
"""
import collections
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        # we want a counter
        size = len(S)
        cd = collections.defaultdict(int)
        limit = size//2+1 if size%2 else size//2
        maxCnt, mostFreq = 0, ""
        for c in S:
            cd[c] += 1
            if cd[c] > limit:
                return ""
            if cd[c] > maxCnt:
                maxCnt, mostFreq = cd[c], c

        return self.org(cd, mostFreq, size)

    def org(self, cd, k, size):
        
        fo = [i for i in range(0, size, 2)] + [i for i in range(1, size, 2)]        # filling order
        res = ["" for _ in range(size)]
        i = 0
        
        while cd[k]:                        # fill k first
            res[fo[i]], i = k, i+1
            cd[k] -= 1

        keys = cd.keys()
        for k in keys:
            while cd[k]:
                res[fo[i]], i = k, i+1
                cd[k] -= 1
        return ''.join(res)

print Solution().reorganizeString('aab')
print Solution().reorganizeString('aaab')
print Solution().reorganizeString('aabb')
print Solution().reorganizeString("aaaaaaaabbccdef")
print Solution().reorganizeString("vvvlo")
print Solution().reorganizeString("baaba")
