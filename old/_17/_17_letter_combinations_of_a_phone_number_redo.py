"""
17. Letter Combinations of a Phone Number

    Total Accepted: 103311
    Total Submissions: 332208
    Difficulty: Medium

Given a digit string,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numdict = {"1":[], "2":["a","b","c"], "3":["d","e","f"],
        "4":["g","h","i"], "5":["j","k","l"], "6"::["m","n","o"],
        "7":["p","q","r","s"], "8"::["t","u","v"], "9":["w","x","y","z"]}
        res = []
        if not digits:
            return []
        if len(digits) == 1:
            return [c for c in numdict[digits[0]]]
        
        thisNum = numdict[digits[0]]
        restNums = self.letterCombinations(digits[1:])

        return [t+c for t in thisNum for c in restNums]
