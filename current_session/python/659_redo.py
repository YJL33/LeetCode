from typing import List
import collections

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # consecutive subsequence must have len >= 3
        if len(nums) < 3: return False

        # naive approach:
        # make subsequences if needed, and verify while need to close
        # if there's a duplicate: must use 2nd subsequence
        # verify the last number as well, if not consecutive: need to close

        dq = collections.deque()

        for n in nums:
            # remove terminated subsequences
            while dq and dq[0][0]+1 < n:
                lastN, seqLen = dq.popleft()
                if seqLen < 3: return False

            # add into existing subsequence
            stash = []
            while dq and dq[0][0] == n:
                stash.append((dq.popleft()))
            while len(dq) >= 2 and dq[1][0] == n-1 and dq[0][1] >= 3:
                stash.append((dq.popleft()))
            if dq:
                lastN, seqLen = dq.popleft()
                # print('lastN:', lastN)
                assert(lastN == n-1)
                dq.append((n, seqLen+1))
            else:
                dq.append((n, 1))
            while stash:
                dq.appendleft(stash.pop())

        return all([x >= 3 for _, x in dq])

print(Solution().isPossible([1,2,2,3,3,3,4,5]), "should be False")
print(Solution().isPossible([1,2,2,3,3,3,4,4,5]), "should be True")
print(Solution().isPossible([1,2,2,3,3,3,4,4,4,5]), "should be True")
print(Solution().isPossible([1,2,3,3,4,5]), "should be True")
print(Solution().isPossible([1,2,3,4,4,5]), "should be False")
print(Solution().isPossible([1,2,3,3,4,4,5,5]), "should be True")
print(Solution().isPossible([1,2,3]), "should be True")
print(Solution().isPossible([1,3,3,4,4,7,8,8,9,10]), "should be False")
print(Solution().isPossible([1,2,3,4,6,7,8,9,10,11]), "should be True")
