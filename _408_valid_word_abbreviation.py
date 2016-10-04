"""
408. Valid Word Abbreviation

    User Accepted: 1
    User Tried: 8
    Total Accepted: 1
    Total Submissions: 12
    Difficulty: Easy

Given a non-empty string s and an abbreviation abbr,
return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

Notice that only the above abbreviations are valid abbreviations of the string "word".
Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:

Given s = "internationalization", abbr = "i12iz4n":

Return true.

Example 2:

Given s = "apple", abbr = "a2e":

Return false.
"""
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i, j = i+1, j+1
            elif 49 <= ord(abbr[j]) <= 57:
                num = 0
                while j < len(abbr) and 48 <= ord(abbr[j]) <= 57:
                    num, j = 10*num+int(abbr[j]), j+1
                if i + num > len(word): return False
                i += num
            else:
                return False

        if i != len(word) or j != len(abbr): return False
        return True