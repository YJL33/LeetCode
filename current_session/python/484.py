from typing import List
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        # thoughts
        # for n number permutations, use n-1 characters to represent, from "II...II" to "DD...DD"
        #
        # brute force:
        # convert D/I into x-th permutation, and generate it (next, next ....)
        #
        # optimization:
        # can we generate in-place?
        # use stack
        # tc: O(n)
        # sc: O(size of stack), worse case O(n)

        s += "I"
        res, st = [], []
        for i,c in enumerate(s, start=1):
            if c == "I":
                res.append(i)         # check for previous Ds
                while st:
                    res.append(st.pop())
            else:
                st.append(i)
        return res