"""
39
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # sum to target
        # 1 <= candidates <= 200
        # len of candidates <= 30
        # 1 <= target <= 500

        candidates.sort(reverse=True)
        stack = [[(i,c)] for i,c in enumerate(candidates)]
        res = []
        while stack:
            comb = stack.pop()
            s = sum([a[1] for a in comb])
            if s == target:
                res += [a[1] for a in comb],
            elif s < target:
                j = comb[-1][0]
                while target-candidates[j] < 0:
                    j += 1
                while j < len(candidates):
                    stack.append(comb+[(j,candidates[j])])
                    j += 1

        return res

print(Solution().combinationSum([2,3,5],8))
print(Solution().combinationSum([2,3,6,7],7))