"""
see https://leetcode.com/problems/hand-of-straights/
"""
class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W != 0:
            return False

        # pick up from the smallest element
        numOfStraights = len(hand)//W
        i = 0

        cd = {}
        for c in hand:
            if c in cd:
                cd[c] += 1
            else:
                cd[c] = 1

        nums = cd.keys()
        nums.sort()
        i = 0

        while numOfStraights:
            
            while cd[nums[i]] == 0:
                i += 1

            c = nums[i]
            toAdd = W
            while toAdd:
                if c not in cd or cd[c] == 0:
                    return False
                else:
                    cd[c] -= 1
                    toAdd -= 1
                    c += 1

            numOfStraights -= 1

        return True

print(Solution().isNStraightHand([1,2,3,4], 3))
print(Solution().isNStraightHand([3,2,1,2,3,4,3,4,5,9,10,11], 3))
print(Solution().isNStraightHand([3,3,2,2,1,1], 3))
print(Solution().isNStraightHand([1,2,3,3,4,4,5,6], 4))
print(Solution().isNStraightHand([1,2,3,3,4,4,5,6,8,9,10,11,1,2,3,4,2,3,4,5,3,4,5,6],4))
print(Solution().isNStraightHand([2,4,6,8],4))
print(Solution().isNStraightHand([1,2,3,4,6],4))
