from functools import cache
from typing import List
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        # ideas:
        # instead of generate all permutations and then remove those doesn't fit preference
        # we should only generate those permutations that fits preference
        #
        # the ids of hats are distracting, re-order hats and remove those no one likes
        # each hat will have a new ID
        #
        # how to generate?
        # assign each person a preferred hat.
        # if no preferred hat, backtrack
        # (do we assign by hat or by person?) lets assign by hat due to new ID issue
        #
        # helper function (assign hats to person, and also count while assigning)
        # boundary condition: a. no longer need to assign, b. can not assign
        # for a hat, we can either assign or not assign
        # res = number_of_not_assigning + number_of_assigning
        # 
        # e.g. [[3,5,1],[3,5]]
        #      hat 1, 3, 5 -> 0, 1, 2
        #      hat_to_person: {0:[0], 1:[0,1], 2:[0,1]}
        #      
        #      for hatID=0, not assigning: [1,2],[2,1]. assigning [0,1] [0,2]    => overall 4
        #
        htop = [[] for _ in range(41)]  # hat to person 
        for i,pref in enumerate(hats):
            for h in pref:
                htop[h].append(i)
        htop = [h for h in htop if len(h) > 0]
        # print('htop',htop)
        num_of_hats, num_of_person = len(htop), len(hats)
        if num_of_hats < num_of_person: return 0
        
        def count_ones(n):
            if not n: return 0
            cnt = 1 if n&1 else 0
            return count_ones(n>>1)+cnt
        
        # assign ith hat to person
        # mask: if mask&(1<<p) means person p is already assigned a hat
        @cache
        def helper(i, mask):            # we can use bitwise here
            # print('i', i, 'mask', bin(mask)[2:])
            # boundary condition
            if count_ones(mask) == num_of_person: return 1
            if i == num_of_hats: return 0
            res = helper(i+1, mask)
            for person in htop[i]:
                if mask&(1<<person) == 0:
                    mask |= 1<<person
                    res += helper(i+1, mask)
                    mask ^= 1<<person
            return res%(10**9+7)
        
        return helper(0, 0)
