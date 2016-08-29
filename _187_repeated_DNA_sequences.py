"""
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # convert string to bit
        if len(s) < 11: return []
        toInt = {'A':0, 'C':1, 'G':2, 'T':3}
        mask = (1<<20)-1
        key = 0

        sequence = {}
        ans = []
        for i in xrange(9):
            key = (key << 2) + toInt[s[i]]
        for i in xrange(9, len(s)):
            key = ((key << 2) + toInt[s[i]]) & mask
            if key in sequence:
                sequence[key] += 1
                if sequence[key] == 2:
                    ans.append(s[i-9:i+1])
            else:
                sequence[key] = 1
        return ans


