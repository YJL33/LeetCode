"""
134
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start = len(gas)-1      # begin from the last station
        end = 0
        gas_left = gas[start]-cost[start]

        while start > end:
            if gas_left >= 0:
                gas_left += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                gas_left += gas[start] - cost[start]

        if gas_left >= 0:
            return start
        else:
            return -1

print Solution().canCompleteCircuit([3,1,1],[1,2,2])
print Solution().canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2])
