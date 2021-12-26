from typing import List
class Solution:
    # use prefix sum
    def getDistances(self, arr: List[int]) -> List[int]:
        # collect all positions
        # key: element, val: sum of index, cnt of index
        preDict, postDict = {}, {}
        preRes, postRes = [], []
        
        for i in range(len(arr)):
            cur1, cur2 = arr[i], arr[~i]
            if cur1 in preDict:     # seen at left side, add the diff
                tmpSum, cnt = preDict[cur1]
                preRes.append(cnt*i - tmpSum)
                preDict[cur1][0] += i
                preDict[cur1][1] += 1
            else:
                preDict[cur1] = [i, 1]
                preRes.append(0)
            
            if cur2 in postDict:
                tmpSum, cnt = postDict[cur2]
                postRes.append(tmpSum - cnt*(len(arr)-1-i))
                postDict[cur2][0] += (len(arr)-1-i)
                postDict[cur2][1] += 1
            else:
                postDict[cur2] = [len(arr)-1-i, 1]
                postRes.append(0)

        return [preRes[i]+postRes[~i] for i in range(len(arr))]