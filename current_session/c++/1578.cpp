#include <string>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int minCost(string s, vector<int>& cost) {
    long minCost=0;
    int prevI=0, cur=0;
    int subSum = cost[0], localMax = cost[0];
    for (int i=1;i<s.size(); ++i) {
      if (s[i] == s[prevI]) {
        subSum += cost[i];
        localMax = max(cost[i], localMax);
        cur = i;
      } else {
        if (cur != prevI) {
          minCost += (subSum - localMax);
        }
        cur = i;
        prevI = i;
        localMax = cost[i];
        subSum = cost[i];
      }
    }
    if (cur != prevI) minCost += subSum - localMax;
    return int(minCost);
  }
};