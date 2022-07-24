import heapq
class Solution:
    def minimumDeviation(self, A):
        max_hp = []         # for even numbers
        min_seen = float('inf')
        for a in A:
            if a%2:
                max_hp.append(-1*a*2)
                min_seen = min(min_seen, 2*a)
            else:
                max_hp.append(-1*a)
                min_seen = min(min_seen, a)
        heapq.heapify(max_hp)
        
        min_dev = -max_hp[0]-min_seen
        while max_hp[0]%2 == 0:
            val = heapq.heappop(max_hp)
            val = (-1*val)//2
            heapq.heappush(max_hp, -1*val)
            min_seen = min(min_seen, val)
            min_dev = min(min_dev, -max_hp[0]-min_seen)
        
        return min_dev
        