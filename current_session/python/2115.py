from typing import List
import collections
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # keep update the supplies when we know that we can supply certain recipe.
        # another via approach: implement topological sort (kahn's algorithm)
        ss = set(supplies)
        rd = collections.defaultdict(set)
        for i in range(len(recipes)):
            r, loi = recipes[i], ingredients[i]
            rd[r] = set(loi)
        
        res = set()
        checked = [False for _ in recipes]
        while True:
            toAdd = set()
            for i in range(len(recipes)):
                r = recipes[i]
                if not checked[i] and rd[r].issubset(ss):
                    toAdd.add(r)
                    res.add(r)
                    checked[i] = True
            ss = ss.union(toAdd)
            if not toAdd: break
        
        return list(res)


        
                
print(Solution().findAllRecipes(["ju","fzjnm","x","e","zpmcz","h","q"],[["d"],["hveml","f","cpivl"],["cpivl","zpmcz","h","e","fzjnm","ju"],["cpivl","hveml","zpmcz","ju","h"],["h","fzjnm","e","q","x"],["d","hveml","cpivl","q","zpmcz","ju","e","x"],["f","hveml","cpivl"]],["f","hveml","cpivl","d"]))
print('should be ["ju","fzjnm","q"]')