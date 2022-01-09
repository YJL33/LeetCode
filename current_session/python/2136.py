from typing import List
class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # sort based on grow Time
        gt = []
        for i in range(len(growTime)):
            gt.append((growTime[i], i))
        gt.sort(reverse=True)
        total_plant_time = sum(plantTime)
        bloom_days = []
        for t, i in gt:
            total_plant_time -= plantTime[i]
            bloom_days.append(total_plant_time-t)
        
        return sum(plantTime)-min(bloom_days)
