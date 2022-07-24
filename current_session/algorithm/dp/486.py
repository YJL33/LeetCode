from functools import cache
from typing import List
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # both players are playing optimally =>
        # player should choose a number that makes the next one has smaller choice (?)

        # say player 1 move first (A), and then player 2 move (B)
        # if player 2 can win on move (B) => 
        # player 1 can't win on move (A) if score obtained in A can not overcome B's situation

        # return the score of arr, with who's turn
        @cache
        def get_score(start, end):
            if start == end:
                return [nums[start], 0]
            elif start+1 == end:
                return [max(nums[start], nums[end]), min(nums[start], nums[end])]
            else:
                lb, la = get_score(start+1, end)
                la += nums[start]
                rb, ra = get_score(start, end-1)
                ra += nums[end]
                if la >= ra:
                    return [la, lb]
                else:
                    return [ra, rb]
        
        score = get_score(0, len(nums)-1)
        assert(sum(score) == sum(nums))
        print('score', score)
        return score[0] >= score[1]
        
print(Solution().PredictTheWinner([7,7,7,7,1,1,1,1]))
print(Solution().PredictTheWinner([9,9,9,9,9,9]))
print(Solution().PredictTheWinner([9,9,9,9,9,9,8,8,8,8,8,8,2,2,2,2,1,1]))