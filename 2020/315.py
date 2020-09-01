"""
see https://leetcode.com/problems/count-of-smaller-numbers-after-self/
"""
import heapq
import bisect
class Solution(object):

        # the naive approach: count each point
        # time complexity: O(n^2)

        # DP:
        # start from the right and fill each spot.
        #
        # psuedo code:
        # smaller, bigger   stores seen elements that are either smaller or bigger than current element
        # smaller: the biggest one is the root of the heap (maxHeap)
        # bigger: the smallest one is the root of the heap (minHeap)
        # for r in nums[::-1]:
        #   if smaller and smaller[0] >= r:
        #       bigger.push(smaller.pop(0))
        #   if bigger and bigger[0] < r:
        #       smaller.push(bigger.pop(0))
        #   dp[r] = len(smaller)
        #   smaller += r,

    def countSmaller_DP(self, nums):                # (TLE!!)
        if not nums: return []

        dp = [i for i in range(len(nums)-1,-1,-1)]  # max number of count
        # print(dp)
        minHeap, maxHeap = [], []                   # make maxHeap always slightly bigger
        for r in range(len(nums)-1, -1, -1):
            while maxHeap and (-1)*maxHeap[0] >= nums[r]:
                heapq.heappush(minHeap, (-1)*heapq.heappop(maxHeap))
            while minHeap and minHeap[0] < r:
                heapq.heappush(minHeap, (-1)*heapq.heappop(minHeap))
            print("r:", nums[r], "maxH", [-1*x for x in maxHeap], "minH", minHeap)
            dp[r] = len(maxHeap)
            heapq.heappush(maxHeap, (-1)*nums[r])
        return dp


        # count jumps while doing merge sort
    def countSmaller_MS(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [0 for _ in nums]
        print([(nums[i], i) for i in range(len(nums))])

        def mSort(arr):
            if len(arr) <= 1:
                return arr
            l, r = mSort(arr[:(len(arr)/2)]), mSort(arr[(len(arr)/2):])
            res, i, j = [], 0, 0
            while i < len(l) or j < len(r):
                print l, r, i, j
                if j == len(r) or (i < len(l) and l[i][0] <= r[j][0]):
                    ans[l[i][1]] += j
                    res = res + [l[i]]
                    i += 1
                else:
                    res = res + [r[j]]
                    j += 1
            print("output:", res)
            print("ans now:", ans)
            return res

        mSort([(nums[i], i) for i in range(len(nums))])
        return ans

        # prepare an empty array (which will put the sorted nums inside)
        # pick from backward and use bisect to find the index to insert
        # the length before the insert position is the count
        # time comlexity: O(n*logn)
    def countSmaller(self, nums):
        tmp = []
        ans = [0 for _ in nums]
        for i in range(len(nums)-1, -1, -1):
            pos = bisect.bisect(tmp, nums[i])
            tmp.insert(pos, nums[i])
            # print(res)
            while pos > 0 and tmp[pos] == tmp[pos-1]:
                pos -= 1
            ans[i] = pos
            # print(ans)
        return ans

# print(Solution().countSmaller([1,2,3,4,5,4,3,2,1]) == Solution().countSmaller_DP([1,2,3,4,5,4,3,2,1]))
# print(Solution().countSmaller([1,2,3,4,5,4,3,2,1]))
# print(Solution().countSmaller([1,2,3,4,5,6,7,8,9]))
print(Solution().countSmaller([1,2,3,4,5,6,7,8,9][::-1]))
