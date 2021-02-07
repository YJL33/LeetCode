"""
636
"""
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        # n functions, from 0 to n-1
        # simply simulate

        i = 0
        res = [0 for _ in range(n)]
        sStack, eStack = [], []
        while i < len(logs):
            cId, eventType, sec = logs[i].split(':')
            if eventType == 'start':
                if sStack:
                    pId, st = sStack.pop()
                    res[pId] += int(sec)-st
                    eStack.append(pId)
                sStack.append((int(cId), int(sec)))
            else:
                pId, st = sStack.pop()
                # assert(pId == int(cId))
                res[pId] += int(sec)-st+1
                if eStack:
                    pId = eStack.pop()
                    sStack.append((pId, int(sec)+1))
            i += 1
        
        return res

print(Solution().exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))