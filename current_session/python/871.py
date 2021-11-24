from typing import List
import collections
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # use DP
        if target > startFuel+sum([f for _, f in stations]): return -1
        if not stations: return 0 if startFuel >= target else -1

        # DP / dict (times of refuel)
        # key = refill times, value: remaining Fuel

        trips = {0:startFuel}
        pos, i = 0, 0
        minRefill = float('inf')

        while pos < target and i < len(stations):
            stationPosition, stationFuel = stations[i]
            tmp = collections.defaultdict()
            # print('trips:', trips, 'min refills:', minRefill, 'pos:', pos, 'dis', stationPosition-pos)

            for refills, remainingFuel in trips.items():
                # print('refill, fuel, pos', refills, remainingFuel, pos)
                if pos + remainingFuel >= target:
                    minRefill = min(minRefill, refills)
                elif refills > minRefill or pos + remainingFuel < stationPosition:
                    continue
                else:
                    dist = stationPosition-pos
                    if refills in tmp:
                        tmp[refills] = max(tmp[refills], remainingFuel-dist)
                    else:
                        tmp[refills] = remainingFuel-dist
                    if refills+1 in tmp:
                        tmp[refills+1] = max(tmp[refills+1], remainingFuel-dist+stationFuel)
                    else:
                        tmp[refills+1] = remainingFuel-dist+stationFuel

            pos, trips = stationPosition, tmp
            i += 1
            # print('trips now:', trips, 'at pos: ', pos)
        
        # print('trips:', trips, 'min refills:', minRefill, 'pos:', pos, 'i', i)
        if pos < target and i == len(stations):
            for refills, remainingFuel in trips.items():
                if pos + remainingFuel >= target:
                    minRefill = min(minRefill, refills)
            return -1 if minRefill == float('inf') else minRefill

        return min([k for k, _ in trips])

# print(Solution().minRefuelStops(1,1,[]))
# print(Solution().minRefuelStops(100,1,[[10,100]]))
# print(Solution().minRefuelStops(100,10,[[10,60], [20,30], [30,30], [60,40]]))
print(Solution().minRefuelStops(1000,1,[[1,186],[145,161],[183,43],[235,196],[255,169],[263,200],[353,161],[384,190],[474,44],[486,43],[567,48],[568,96],[592,36],[634,181],[645,167],[646,69],[690,52],[732,28],[800,42],[857,55],[922,63],[960,141],[973,13],[977,112],[997,162]]))