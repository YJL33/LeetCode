import itertools
from typing import List
import collections
class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        # count the pairs of each row
        # e.g.
        # [[1,0,0,1,0],         found (0,3). pair_dict[(0,3)] += 1
        #  [0,0,1,0,1],         found (2,4). pair_dict[(2,4)] += 1
        #  [0,0,0,1,0],         not found any
        #  [1,0,1,0,1]]         found (0,2),(0,4),(2,4) => res+1, update the dict

        # time complexity: O(N) * O(M^2), 
        # where N is the number of row, and M is the length of row, 
        # (O(M^2) is the complexity to find all pairs in the row)

        count = 0
        pair_dict = collections.defaultdict(int)

        def get_pairs(row):        # return a list of tuple
            ones = []
            for i, v in enumerate(row):
                if v == 1: ones.append(i)
            return itertools.combinations(ones, 2)

        for r in grid:
            pairs = get_pairs(r)
            for p in pairs:
                if p in pair_dict:
                    count += pair_dict[p]
                pair_dict[p] += 1
        
        return count

