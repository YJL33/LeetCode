import collections
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # instead of remove duplicates from generated permutations,
        # generate unique permutations only
        #
        # e.g. ['aaaabbccc'], count of a: 4, b: 2, c:3
        # the solution is to try use a/b/c each as 1st characeter:
        # = ['a'] + permuteUnique('aaabbccc') + ['b'] + permuteUnique('aaaabccc') + ['c'] + permuteUnique('aaaabbcc')
        # .......
        #
        # analysis:
        # use a global list res to store outputs
        # directly generate the output
        # tc: O(X), where X is the size of output
        # sc: O(X), where X is the size of output
        
        def helper(counter):
            if not counter or len(counter) == 0: return []
            tmp, keys = [], [k for k in counter.keys()]

            for k in keys:
                counter[k] -= 1
                if counter[k] == 0: del counter[k]

                suffix = helper(counter)
                if not suffix:
                    tmp.append([k])
                else:
                    for s in suffix:
                        tmp.append([k]+s)

                counter[k] += 1
                
            return tmp
    
        res = helper(collections.Counter(nums))
        return res
            