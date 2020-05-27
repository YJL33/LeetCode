"""
49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return: [["ate", "eat","tea"],["nat","tan"],["bat"]]

Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        import bisect

        def getStrSig(s):
            """
            get the signature of str s
            """
            primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
            ord_a = ord('a')
            hashval = 1
            for c in s: hashval *= primes[ ord(c) - ord_a ]
            return hashval

        worddict = {}
        for s in strs:
            sig = getStrSig(s)    # Here use:  sig = ''.join(sorted(s))  still beats 93.9%
            if sig not in worddict:
                worddict[sig] = [s]
            else:
                bisect.insort_left(worddict[sig], s)    # insert the anagram with correct order
        return worddict.values()