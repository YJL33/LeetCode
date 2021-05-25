"""
411. Minimum Unique Word Abbreviation

    User Accepted: 0
    User Tried: 0
    Total Accepted: 0
    Total Submissions: 0
    Difficulty: Medium

A string such as "word" contains the following abbreviations:

["word", "2rd", "w2d", "wo2", "3d", "w3", "4"]

Given a target string and a set of strings in a dictionary,
find an abbreviation of this target string with the smallest possible length,
such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1.

For example, the abbreviation "a32bc" has length = 4.

Note:

    In the case of multiple answers as shown in the second example below,
    you may return any one of them.
    Assume length of target string = m, and dictionary size = n.
    You may assume that m <= 21,
    n <= 1000, and log2(n) + m <= 20.

Examples:

"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3"
(other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
"""
class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        # first, generate all abbs (with correct order), and then check confliction
        # only generate useful ones
        for i in xrange(len(target), 0, -1):
            abb = str(i)
            return self.isConflict(abb, dictionary)

            if i < len(target):
                for j in xrange(len(target)-i):
                    abb = target[:j] + str(i) + target[j+i:]
                    return self.isConflict(abb, dictionary)

    def isConflict(self, abb, dictionary):
        

        