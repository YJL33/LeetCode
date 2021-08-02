#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
  bool checkSubarraySum(vector<int>& nums, int k) {
    if (nums.size() < 2) return false;
    map<int, int> m;      // use array => MLE
    m[0] = -1;
    int lsum = 0;
    for (int i=0; i<nums.size(); ++i) {
      lsum = (lsum+nums[i])%k;
      if (m.find(lsum) != m.end()) {
        if (i-m[lsum] >= 2) return true;
      } else {
        m[lsum] = i;
      }
    }
    return false;
  }
};