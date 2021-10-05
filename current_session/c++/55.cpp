#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  bool canJump(vector<int>& nums) {
    int canReach = 0;
    int i = 0;
    while (i < nums.size() && i <= canReach) {
      canReach = max(canReach, i+nums[i]);
      if (canReach == nums.size()-1) return true;
      i++;
    }
    return (canReach >= nums.size()-1);
  }
};