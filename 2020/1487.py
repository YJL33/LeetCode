class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        namesDict = {}
        res = []
        for i in xrange(len(names)):
            n = names[i]
            if n not in namesDict:
                namesDict[n] = 1
                res += n,
            else:
                x = namesDict[n]
                newName = n + "(" + str(x) + ")"
                while newName in namesDict:
                    x, newName = x+1, n + "(" + str(x+1) + ")"
                namesDict[n], namesDict[newName] = x, 1
                res += newName,
                    
        return res
