"""
370. Range Addition

    Total Accepted: 4016
    Total Submissions: 7857
    Difficulty: Medium

Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet:
[startIndex, endIndex, inc] which increments each element of subarray:
A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

(Check the examples at Leetcode)
"""
class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # At start record (+incremet), and end+1 record (-increment)
        res = [0]*length
        for op in updates:
            res[op[0]] += op[2]
            if op[1]+1 < length:
                res[op[1]+1] -= op[2]
        temp = 0
        for i in xrange(len(res)):
            temp += res[i]
            res[i] = temp
    
        return res



    def getModifiedArray2(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        # TLE
        ls, arr = [0]*length, array.array('l')
        arr.fromlist(ls)
        for op in updates:
            for i in xrange(op[0], op[1]+1):
                res[i] += op[2]
        return res
