"""
17. Letter Combinations of a Phone Number

Given a digit string,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

 1    2    3
     abc  def
 4    5    6
ghi  jkl  mno
 7    8    9
pqrs tuv  wxyz
 *    0    #

e.g.
    Input: Digit string "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Note:
Although the above answer is in lexicographical order,
your answer could be in any order you want.
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # using recursive
        dct = {'1':'1', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', \
                '7':'pqrs', '8':'tuv', '9':'wxyz', '0':'0'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [ch for ch in dct[digits[0]]]

        prev = self.letterCombinations(digits[:-1])
        new = dct[digits[-1]]

        return [p+n for p in prev for n in new]
