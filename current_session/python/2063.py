class Solution:
    def countVowels(self, word: str) -> int:
        # directly multiply the count of each location
        # e.g. "a" [1]
        # e.g. "ab" [22]
        # e.g. "aba" [343]
        # e.g. "abcd" [4664] a ab abc abcd | 4 + bcd abcd
        # e.g. "abcde" [58985] a ab abc abcd abcde | 6 + bcde abcde
        cnt = 0
        l, r = 1, len(word)
        for i in range(len(word)):
            if word[i] in 'aeiou':
                cnt += l*r
            l, r = l+1, r-1
        return cnt
