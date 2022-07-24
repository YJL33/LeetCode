# first craft a number->letter Dictionary
# use recursion

from typing import List
class Solution:
    def letterCombinations(self, digits:str) -> List[str]:
        if not digits: return []
        numberToLetterDict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        prefixLetters = numberToLetterDict[digits[0]]
        tmp = self.letterCombinations(digits[1:])
        res = []
        for c in prefixLetters:
            if tmp:
                for t in tmp:
                    res.append(c+t)
            else:
                res.append(c)
        return res

print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"))