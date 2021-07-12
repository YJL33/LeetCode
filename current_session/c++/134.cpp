#include <iostream>
#include <vector>

using namespace std;

// naive approach
// find the location with the biggest difference(gas-cost) and start from there,
// won't work if exist some huge cost that needs a lot of accumulation.
// if not working: extend ahead (pick the one ahead), if reach a loop, then it's impossible.
// maybe we can start from anywhere (?)

class Solution {
public:
  int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
    int start = 0;
    int cur = 0;
    int end = gas.size()-1;
    int oil = gas[0];
    while (cur != end) {
      // check if current gas tank is enough to reach next station or not
      int need = cost[cur];

      // simply simulate here
      if (oil<need) {
        start -= 1;
        if (start < 0) start += gas.size();
        end -= 1;
        oil += gas[start];
        oil -= cost[start];
      } else {
        oil -= cost[cur];
        cur += 1;
        oil += gas[cur];
      }
    }
    // check if we can reach the start from end (as the final step)
    return (oil > 0) ? start : -1;
  }
};