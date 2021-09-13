# naive approach
# fill row by row

from typing import List
class Solution:
    def wordsTyping(self, A: List[str], rows: int, cols: int) -> int:
        # craft the 'sentence' and count the index
        sen = ' '.join(A) + ' '
        L = len(sen)
        i = 0

        for _ in range(rows):
            i += cols-1             # move to the end of row
            if sen[i%L] == ' ':
                i += 1
            elif sen[(i+1)%L] == ' ':
                i += 2
            else:
                while i >= 0 and sen[(i-1)%L] != ' ':
                    i -= 1

        return i//L

print(Solution().wordsTyping(sentence = ["hello","world"], rows = 2, cols = 8))
print(Solution().wordsTyping(sentence = ["a", "bcd", "e"], rows = 3, cols = 6))
print(Solution().wordsTyping(sentence = ["i","had","apple","pie"], rows = 4, cols = 5))