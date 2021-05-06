"""
690
"""
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        idict = {}          # important dict
        subdict = {}        # subordinate dict
        for e in employees:
            idict[e.id] = e.importance
            subdict[e.id] = e.subordinates
        
        res = idict[id]
        stack = subdict[id]
        while stack:
            s = stack.pop()
            res += idict[s]
            stack += subdict[s]
        
        return res
            