"""
https://leetcode.com/problems/daily-temperatures/
"""
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # go through the arr
        # for each t in T
        # if increasing (t1 < t2): put t1=1
        # meanwhile pop stack if anything fits
        # if equal or decreasing: 
        # put t1 into stack
        stack = []
        ans = [0 for _ in T]

        for i in range(len(T)-1):
            if T[i+1] > T[i]:
                ans[i] = 1
                while stack and T[i+1] > T[stack[-1]]:
                    j = stack.pop()
                    ans[j] = i+1-j
            else:
                stack += i,

        return ans
print Solution().dailyTemperatures(T = [73, 74, 75, 71, 69, 72, 76, 73])
