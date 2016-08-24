"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Use strs[0] as basis, compare the first letter in rest elements,
        # if all same, compare the second and so on.
        # if find one differet, output the result
        if not strs: return ''
        i, res, isComplete = 0, '', False

        while not isComplete and i < len(strs[0]):      # make sure the index is correct
            char = strs[0][i]
            for s in strs[1:]:                          # compare the rest
                if i >= len(s) or s[i] != char:         # find one different (or missing)
                    isComplete = True
                    return res                          # output the result
            res += char
            i += 1

        return res