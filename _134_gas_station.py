"""
134. Gas Station

There are N gas stations along a circular route,
where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank,
and it costs cost[i] of gas to travel from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once,
otherwise return -1.

Note:
The solution is guaranteed to be unique. 
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
