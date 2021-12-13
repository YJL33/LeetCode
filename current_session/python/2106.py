from typing import List
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        # map fruits to this new array
        # ignore fruits out of bound
        arr = [0 for _ in range(2*k+1)]
        for pos, numOfFruit in fruits:
            if pos < startPos-k or pos > startPos+k:
                continue
            arr[pos-(startPos-k)] += numOfFruit
        
        left, right = sum(arr[:k+1]), sum(arr[k:])
        maxSeen = max(left, right)
        
        turn = 1                            # turning point
        for i in range(2, k+1, 2):
            left = left-arr[i-2]-arr[i-1]+arr[k+turn]
            right = right-arr[~(i-2)]-arr[~(i-1)]+arr[k-turn]
            maxSeen = max(maxSeen, left, right)
            turn += 1
        
        return maxSeen

print(Solution().maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]],5,4))
print(Solution().maxTotalFruits([[200000,10000]],0,200000))
print(Solution().maxTotalFruits([[2,8],[6,3],[8,6]],5,4), 'should be 9')
print(Solution().maxTotalFruits([[0,15],[1,2],[2,7],[3,65],[4,14],[5,49],[6,5],[7,27],[8,71],[9,6],[10,62],[11,15],[12,24],[13,51],[14,22],[15,79],[17,98],[18,46],[19,91],[21,42],[22,31],[23,29],[24,95],[25,96],[27,94],[28,28],[30,62],[31,63],[32,94],[33,27],[34,60],[35,97],[36,1],[37,57],[39,8],[40,92],[41,86],[42,37],[43,48],[44,3],[45,70],[46,64],[47,9],[49,100],[50,33],[51,70],[52,18],[54,37],[55,100],[56,61],[57,33],[58,10],[59,27],[60,37],[61,77],[62,59],[64,30],[65,7],[66,57],[67,5],[68,57],[69,13],[70,15],[71,95],[72,19],[73,50],[74,33],[75,20],[76,72],[77,95],[78,9],[79,18],[80,85],[82,95],[84,85],[86,14],[87,26],[88,68],[91,61],[92,24],[93,32],[94,29],[95,77],[97,100],[99,59],[100,67]],50,125))
print(Solution().maxTotalFruits([[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]],21,30), 'should be 71')