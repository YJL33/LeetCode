
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

from typing import List
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        impDict = {}            # key: id, val: importance
        subDict = {}            # key: id, val: list of subordinates
        for e in employees:
            impDict[e.id] = e.importance
            subDict[e.id] = e.subordinates
        
        res = impDict[id]
        stack = subDict[id]
        while stack:
            x = stack.pop()
            res += impDict[x]
            stack += subDict[x]
        
        return res
