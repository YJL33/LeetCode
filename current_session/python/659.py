"""
see https://leetcode.com/problems/split-array-into-consecutive-subsequences/
"""
class Solution(object):
    def isPossible(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        # consecutive subsequence must have len >= 3
        if len(A) < 3: return False

        # naive approach:
        # make subsequences if needed, and verify while need to close
        # if there's a duplicate: must use 2nd subsequence
        # verify the last number as well, if not consecutive: need to close

        cnt = {}
        for i in range(len(A)):             # O(n)
            if A[i] not in cnt:
                cnt[A[i]] = 1
            else:
                cnt[A[i]] += 1

        ns = cnt.keys()
        ns.sort()

        subs = []
        i = 0                               # subs that's still open (alive)
        last = None

        for n in ns:
            if not last: last = n

            # number to close/add
            na = cnt[n]-len(subs[i:])
            nc = (-1)*na if n-last <= 1 else len(subs[i:])                  # check consecutive

            if nc > 0:       
                if not all([l >= 3 for l in subs[i:i+nc]]): return False    # check length while closing
                i += nc

            if na > 0:
                subs = subs + [0 for _ in range(na)]
            
            # add length to open subs
            for j in range(i, len(subs)):
                subs[j] += 1
            
            # print("after: n, cnt[n], toAdd, open, i, subs", n, cnt[n], toAdd, len(subs[i:]), i, subs)
            last = n

        return all([l >= 3 for l in subs[i:]])

print(Solution().isPossible([1,2,2,3,3,3,4,5]), "should be False")
print(Solution().isPossible([1,2,2,3,3,3,4,4,5]), "should be True")
print(Solution().isPossible([1,2,2,3,3,3,4,4,4,5]), "should be True")
print(Solution().isPossible([1,2,3,3,4,5]), "should be True")
print(Solution().isPossible([1,2,3,4,4,5]), "should be False")
print(Solution().isPossible([1,2,3,3,4,4,5,5]), "should be True")
print(Solution().isPossible([1,2,3]), "should be True")
print(Solution().isPossible([1,3,3,4,4,7,8,8,9,10]), "should be False")
print(Solution().isPossible([1,2,3,4,6,7,8,9,10,11]), "should be True")
