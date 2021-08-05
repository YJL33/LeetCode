#include <iostream>
#include <vector>
#include <map>

using namespace std;

// use a map to store partial sum
class Solution {
public:
  int subarraySum(vector<int>& nums, int k) {
    map<int, int> m;      // key: partial sum, val: count
    m[0] = 1;
    int cnt = 0, lsum = 0;
    for (int i=0; i<nums.size(); ++i) {
      lsum += nums[i];
      if (m.find(lsum-k) != m.end()) {
        cnt += m[lsum-k];
      }
      m[lsum] += 1;
    }
    return cnt;
  }
};