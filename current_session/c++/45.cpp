#include <iostream>

using namespace std;

class Solution {
public:
  int jump(vector<int>& nums) {
    int canReach = 0, end = 0, jp = 0;
    // check from nums[0] to nums[-2]
    for (int i=0; i<nums.size()-1; ++i) {
      canReach = max(canReach, i+nums[i]);
      // increase one until needed
      if (i == end) {
        jp += 1;
        end = canReach;
      }
    }
    return jp;
  }
};