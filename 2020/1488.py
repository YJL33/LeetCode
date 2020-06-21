class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        res = [-1 if x > 0 else 1 for x in rains]
        lakeDict = {}
        lakeDict[0] = []
        need = []
        for i in xrange(len(rains)):
            r = rains[i]
            if r == 0:
                lakeDict[0] += i,
                continue
            if r not in lakeDict:
                lakeDict[r] = [i]
            else:
                need += lakeDict[r][-1],
                if len(need) > len(lakeDict[0]):
                    return []
                
                # we should use the 0 which happens after need
                b = need.pop(0)
                j = 0
                while j < len(lakeDict[0]) and lakeDict[0][j] < b:
                    j += 1
                if j >= len(lakeDict[0]):
                    return []

                res[lakeDict[0].pop(j)] = rains[b]
                lakeDict[r] += i,

        return res


print Solution().avoidFlood([1,0,2,3,0,1,2]) == [-1,1,-1,-1,2,-1,-1], Solution().avoidFlood([1,0,2,3,0,1,2])
print Solution().avoidFlood([1,2,3,0,4]), Solution().avoidFlood([1,2,3,0,4])
print Solution().avoidFlood([1,1,0,0]) == [], Solution().avoidFlood([1,1,0,0])
print Solution().avoidFlood([1,0,2,0,2,1]) == [-1,1,-1,2,-1,-1], Solution().avoidFlood([1,0,2,0,2,1])
print Solution().avoidFlood([1,2,0,2,3,0,1]) == [-1,-1,2,-1,-1,1,-1], Solution().avoidFlood([1,2,0,2,3,0,1])