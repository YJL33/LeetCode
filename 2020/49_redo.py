
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # use a letter counter. O(n*l) where n is len(strs), l is avg length of string

        dct = {}
        for i in range(len(strs)):
            cntArr = [0 for _ in range(26)]
            for c in strs[i]:
                cntArr[ord(c)-97] += 1
            # k = "".join([str(x) for x in cntArr])   # cannot use join -> may have hash clash
            k = tuple([str(x) for x in cntArr])
            if k in dct:
                dct[k] += strs[i],
            else:
                dct[k] = [strs[i]]

        return dct.values()

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))