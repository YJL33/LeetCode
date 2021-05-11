"""
843
"""
# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import collections
import itertools
from typing import List
masterString = 'Master'
class Solution:
    # sort the wordlist by how common characters appear in each spot
    # guess the most common one first
    # based on the output, shorten the list (by removing impossible words)
    # repeat
    def findSecretWord(self, wordlist: List[str], master: masterString) -> None:
        x = 0
        while x < 6:
            cnt = collections.Counter(w1 for w1, w2 in itertools.permutations(wordlist, 2) if self.match(w1, w2) == 0)
            guess = min(wordlist, key=lambda w: cnt[w])
            x = master.guess(guess)
            wordlist = [w for w in wordlist if self.match(w, guess) == x]

    # compare two words and return the count of same character in same position
    def match(self, w1, w2):
        return sum(i == j for i, j in zip(w1, w2))