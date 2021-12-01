import collections
class Solution:
    def minSteps(self, n: int) -> int:
        # factorization of integer
        if n == 1: return 0
        dp = [i for i in range(n+1)]
        for i in range(2, n+1):
            for j in range(i-1, 1, -1):     # try from the longest possible copy
                if (i%j == 0):
                    dp[i] = dp[j] + (i//j)
                    break
        return dp[-1]

    def minSteps_TLE(self, n: int) -> int:
        # we want n characters of 'A'
        # we can do either copy or paste
        # paste: +length that stored
        # copy: store current length

        # first move must be copy
        if n == 1: return 0
        if n == 2: return 2
        dq = collections.deque()
        dq.append((1,0,0))
        lengthSeen = set()
        while dq:
            currentLength, lengthStored, opsCnt = dq.popleft()
            lengthSeen.add((currentLength, lengthStored))
            if currentLength+lengthStored == n:
                return opsCnt+1
            # do either copy or paste
            # copy
            if currentLength*2 <= n:
                dq.append((currentLength, currentLength, opsCnt+1))
                # print('copy: ', dq[-1])

            # paste
            if (lengthStored%2 == 0 and currentLength%2 == 0 and n%2 == 1): continue
            if (currentLength+lengthStored, lengthStored) not in lengthSeen and currentLength+2*lengthStored<=n:
                dq.append((currentLength+lengthStored, lengthStored, opsCnt+1))
                # print('paste: ', dq[-1])
        
        return -1
            


print(Solution().minSteps(1), 'shoule be 0')
print(Solution().minSteps(2), 'shoule be 2')
print(Solution().minSteps(3), 'shoule be 3')
print(Solution().minSteps(4), 'shoule be 4')
print(Solution().minSteps(999), 'shoule be 46')
print(Solution().minSteps(908), 'shoule be 231')
print(Solution().minSteps(853), 'shoule be 853')
