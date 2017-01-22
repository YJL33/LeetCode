"""
288. Unique Word Abbreviation

    Total Accepted: 15131
    Total Submissions: 96782
    Difficulty: Easy

An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n

Assume you have a dictionary and given a word,
find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
"""
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abb = {}
        self.wordset = set()
        for word in dictionary:
            aka = self.aka(word)
            if word not in self.wordset:    # new word
                self.wordset.add(word)
                if aka not in self.abb:     # new word with new abb.
                    self.abb[aka] = 1
                else:                       # new word with repeated abb.
                    self.abb[aka] += 1

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        aka = self.aka(word)
        if word in self.wordset:            # seen word
            return self.abb[aka] == 1
        if aka in self.abb:                 # un-seen word
            return False
        else:
            return True

    def aka(self, word):
        if len(word) <= 2: return word
        else: return word[0]+str(len(word)-2)+word[-1]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")