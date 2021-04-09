"""
418
"""
from typing import List
class Solution:
    def wordsTyping(self, A: List[str], rows: int, cols: int) -> int:
        # craft the 'sentence' and count the index
        sen = ' '.join(A) + ' '
        L = len(sen)
        i = 0
        # moves = rows*cols
        for _ in range(rows):
            # print('befor', i%L, sen[i%L])
            i += cols-1             # move to the end of row
            if sen[i%L] == ' ':
                i += 1
            elif sen[(i+1)%L] == ' ':
                i += 2
            else:
                while i >= 0 and sen[(i-1)%L] != ' ':
                    i -= 1
            # print('   after', i%L, sen[i%L])
        # print('i',i)
        return i//L

# print(Solution().wordsTyping(rows = 4, cols = 5, A = ["I", "had", "apple", "pie"]))
# print(Solution().wordsTyping(rows = 3, cols = 6, A = ["a", "bcd", "e"]))
# print(Solution().wordsTyping(rows = 2, cols = 8, A = ["hello", "world"]))
print(Solution().wordsTyping(["f","p","a"],8,7))
# print(Solution().wordsTyping(["a"],10000,10000))
