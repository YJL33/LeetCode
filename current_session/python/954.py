import sortedcontainers
import collections
from typing import List

class Solution:
    # clarifications
    # input validity?
    # upperbound/lowerbound of arr[i]?
    # type of arr[i]?
    # length of arr? any restrictions on memory?
    # is arr given sorted?
    # timeouts?
    
    # test cases

    # sort
    # from left to right, seek for 2n, if not exist -> return False
    # handle negatives: all treat as positive
    # use an array length == L to store usage
    # tc: O(nlogn) + O(n)
    # sc: O(n) to store usage
    
    # alternative:
    # use sortedList, after a pair is verified, remove those from sortedlist
    # tc: O(nlogn) to sort, O(n)*O(logn) removals
    # sc: O(n) to use sortedlist, O(n) to use a counter
    def canReorderDoubled_sl(self, arr: List[int]) -> bool:  
        if sum(arr)%3 != 0: return False
        cnt = collections.Counter(arr)
        if cnt[0]%2: return False
        A1 = sortedcontainers.SortedList([a for a in arr if a > 0])
        A2 = sortedcontainers.SortedList([abs(a) for a in arr if a < 0])
        def check(A):
            while A:
                a = A[0]
                i = A.bisect_left(2*a)
                if i >= len(A) or i == 0 or A[i] != 2*a:
                    return False
                A.remove(a)
                A.remove(2*a)
            return True
        return check(A1) and check(A2)

    # use a counter
    # tc: O(N) to count, O(KlogK) to sort, where K is the number of keys, O(K) to verify
    # sc: O(K) to store those keys
    def canReorderDoubled(self, A):
        cnt = collections.Counter(A)
        keys = [k for k in cnt.keys()]
        keys.sort(key=abs)
        for k in keys:
            if cnt[k] > cnt[2*k]:
                return False
            cnt[2*k] -= cnt[k]
        return True