"""
721
"""
from typing import List
import collections
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        md = collections.defaultdict(list)
        pd = {}
        self.root = [i for i in range(len(accounts))]

        def getRoot(i):
            while self.root[i] != i:
                i = self.root[i]
            return i

        for i in range(len(accounts)):
            _, email = accounts[i]
            md[email].append(i)
            if len(md[email]) >= 1:
                prevRoot = getRoot(self.root[i])
                self.root[prevRoot] = getRoot(md[email][0])

        for i in range(len(accounts)):
            if getRoot(i) == i:
                pd[accounts[i][0]] = set()
        
        for j in range(len(accounts)):
            usr = accounts[getRoot(j)][0]
            pd[usr].add(accounts[j][1])
