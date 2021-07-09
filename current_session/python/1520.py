"""
see https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/
"""
class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cd = {}     # charDict
        for i in xrange(len(s)):
            if s[i] not in cd:
                cd[s[i]] = [i]
            else:
                cd[s[i]] += i,

        seen, toCheck = [], []

        # find the range for all characters
        for k in cd.keys():
            toCheck += (cd[k][-1] - cd[k][0] + 1, k),

        # sort them based on length
        toCheck.sort()
        
        # check those chars
        # if within the range there's any char that's already been added, ignore it.
        res = []
        for _, c in toCheck:
            if c in seen: continue
            checker = True
            b, e, cnt = cd[c][0], cd[c][-1], 0
            tmp = []

            # keep update start and end until the range includes all appearances
            while cnt != e-b+1 and checker:
                for x in set(s[b:e+1]):
                    if x in seen:
                        checker = False
                        break
                    if x not in tmp:
                        cnt += len(cd[x])       # add the count (use len!)
                        b, e = min(b, cd[x][0]), max(e, cd[x][-1])
                        tmp += x,
            if checker:
                res += s[b:e+1],
                for y in tmp:
                    seen += y,
            
        return res

print Solution().maxNumOfSubstrings("abbaccd"), "should be ", ["d","bb","cc"]
print Solution().maxNumOfSubstrings("adefaddaccc"), "should be", ["e","f","ccc"]
print Solution().maxNumOfSubstrings("ababa"), "should be", ["ababa"]
print Solution().maxNumOfSubstrings("cbaabaabc"), "should be", ["baabaab"]
print Solution().maxNumOfSubstrings("badadbeabc"), "should be", ["e","c"]
print Solution().maxNumOfSubstrings("cabcccbaa"), "should be", ["cabcccbaa"]
