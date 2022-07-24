from typing import List
import collections
import heapq
class Solution(object):
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # idea:
        # simulate the process
        # count the occurance
        # use heap to decide which one we should put into the result
        # (we need 2 heaps for both frequency and last occurance)
        # put each element into the heap and based on frequency and last_index
        #
        # time complexity: count the occurance O(n), heap operation O(nlogn), for each element, each one at most 3 push/pop
        # space complexity: counter O(n), heap O(T), where T is the number of unique tasks
        cnt = collections.Counter(tasks)
        hp = []
        for task, count in cnt.items():
            heapq.heappush(hp, (-count, task))                  # frequency is negative (due to built-in python heap)
        last_index = {t:float('-inf') for t in task}

        res, tmp = 0, []
        while hp or tmp:
            current_idx = res                                   # current_idx is where we want to put the task
            if hp:
                _, task = heapq.heappop(hp)
                last_index[task], cnt[task] = current_idx, cnt[task]-1
                if cnt[task] != 0:                              # if freq == 0 don't put it back
                    heapq.heappush(tmp, (current_idx, task))
            res += 1
            
            while tmp and last_index[tmp[0][1]]+n < res:
                _, task = heapq.heappop(tmp)
                heapq.heappush(hp, (-cnt[task], task))
            
        return res

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # math
        # ["A","A","A","B","B","B"], n = 2
        # A -> B -> idle -> A -> B -> idle -> A -> B
        # A and B both has maxCount=3
        # observe that in "one round", there's (n+1) in the round
        # in the last round, only elements has the maxCount are in the round
        # we got: (n+1)*(maxCount-1)+numOfElementsHasMaxCount

        taskCnt = collections.defaultdict(int)
        maxSeen = 0
        for t in tasks:
            taskCnt[t] += 1
            if taskCnt[t] >= maxSeen:
                maxSeen = taskCnt[t]

        maxCnt = 0
        for k, v in taskCnt.items():
            if taskCnt[k] == maxSeen:
                maxCnt += 1

        ans = (n+1)*(maxSeen-1)+maxCnt
        return max(len(tasks),ans)      # in case maxSeen = 1

print(Solution().leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],2), 'should be 16')
print(Solution().leastInterval(["A","A","A","B","B","B"],50), 'should be 104')
print(Solution().leastInterval(["A","A","A","B","B","B"], n = 2),'should be 8')
print(Solution().leastInterval(["A","A","A","B","B","B"], n = 0),'should be 6')
print(Solution().leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"],2),'should be 12')
print(Solution().leastInterval(["G","C","A","H","A","G","G","F","G","J","H","C","A","G","E","A","H","E","F","D","B","D","H","H","E","G","F","B","C","G","F","H","J","F","A","C","G","D","I","J","A","G","D","F","B","F","H","I","G","J","G","H","F","E","H","J","C","E","H","F","C","E","F","H","H","I","G","A","G","D","C","B","I","D","B","C","J","I","B","G","C","H","D","I","A","B","A","J","C","E","B","F","B","J","J","D","D","H","I","I","B","A","E","H","J","J","A","J","E","H","G","B","F","C","H","C","B","J","B","A","H","B","D","I","F","A","E","J","H","C","E","G","F","G","B","G","C","G","A","H","E","F","H","F","C","G","B","I","E","B","J","D","B","B","G","C","A","J","B","J","J","F","J","C","A","G","J","E","G","J","C","D","D","A","I","A","J","F","H","J","D","D","D","C","E","D","D","F","B","A","J","D","I","H","B","A","F","E","B","J","A","H","D","E","I","B","H","C","C","C","G","C","B","E","A","G","H","H","A","I","A","B","A","D","A","I","E","C","C","D","A","B","H","D","E","C","A","H","B","I","A","B","E","H","C","B","A","D","H","E","J","B","J","A","B","G","J","J","F","F","H","I","A","H","F","C","H","D","H","C","C","E","I","G","J","H","D","E","I","J","C","C","H","J","C","G","I","E","D","E","H","J","A","H","D","A","B","F","I","F","J","J","H","D","I","C","G","J","C","C","D","B","E","B","E","B","G","B","A","C","F","E","H","B","D","C","H","F","A","I","A","E","J","F","A","E","B","I","G","H","D","B","F","D","B","I","B","E","D","I","D","F","A","E","H","B","I","G","F","D","E","B","E","C","C","C","J","J","C","H","I","B","H","F","H","F","D","J","D","D","H","H","C","D","A","J","D","F","D","G","B","I","F","J","J","C","C","I","F","G","F","C","E","G","E","F","D","A","I","I","H","G","H","H","A","J","D","J","G","F","G","E","E","A","H","B","G","A","J","J","E","I","H","A","G","E","C","D","I","B","E","A","G","A","C","E","B","J","C","B","A","D","J","E","J","I","F","F","C","B","I","H","C","F","B","C","G","D","A","A","B","F","C","D","B","I","I","H","H","J","A","F","J","F","J","F","H","G","F","D","J","G","I","E","B","C","G","I","F","F","J","H","H","G","A","A","J","C","G","F","B","A","A","E","E","A","E","I","G","F","D","B","I","F","A","B","J","F","F","J","B","F","J","F","J","F","I","E","J","H","D","G","G","D","F","G","B","J","F","J","A","J","E","G","H","I","E","G","D","I","B","D","J","A","A","G","A","I","I","A","A","I","I","H","E","C","A","G","I","F","F","C","D","J","J","I","A","A","F","C","J","G","C","C","H","E","A","H","F","B","J","G","I","A","A","H","G","B","E","G","D","I","C","G","J","C","C","I","H","B","D","J","H","B","J","H","B","F","J","E","J","A","G","H","B","E","H","B","F","F","H","E","B","E","G","H","J","G","J","B","H","C","H","A","A","B","E","I","H","B","I","D","J","J","C","D","G","I","J","G","J","D","F","J","E","F","D","E","B","D","B","C","B","B","C","C","I","F","D","E","I","G","G","I","B","H","G","J","A","A","H","I","I","H","A","I","F","C","D","A","C","G","E","G","E","E","H","D","C","G","D","I","A","G","G","D","A","H","H","I","F","E","I","A","D","H","B","B","G","I","C","G","B","I","I","D","F","F","C","C","A","I","E","A","E","J","A","H","C","D","A","C","B","G","H","G","J","G","I","H","B","A","C","H","I","D","D","C","F","G","B","H","E","B","B","H","C","B","G","G","C","F","B","E","J","B","B","I","D","H","D","I","I","A","A","H","G","F","B","J","F","D","E","G","F","A","G","G","D","A","B","B","B","J","A","F","H","H","D","C","J","I","A","H","G","C","J","I","F","J","C","A","E","C","H","J","H","H","F","G","E","A","C","F","J","H","D","G","G","D","D","C","B","H","B","C","E","F","B","D","J","H","J","J","J","A","F","F","D","E","F","C","I","B","H","H","D","E","A","I","A","B","F","G","F","F","I","E","E","G","A","I","D","F","C","H","E","C","G","H","F","F","H","J","H","G","A","E","H","B","G","G","D","D","D","F","I","A","F","F","D","E","H","J","E","D","D","A","J","F","E","E","E","F","I","D","A","F","F","J","E","I","J","D","D","G","A","C","G","G","I","E","G","E","H","E","D","E","J","B","G","I","J","C","H","C","C","A","A","B","C","G","B","D","I","D","E","H","J","J","B","F","E","J","H","H","I","G","B","D"],1),'should be 1000')