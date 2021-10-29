#include <iostream>
#include <vector>

using namespace std;

// clang++ -std=c++17 c++/1567.cpp -o 1567 && ./1567 -v

// for each n in nums, if n == 0: start over again
// if not, focus on the continuous product itself
// e.g. [-,+,+,+,+,+,-,-,-,+,0,+,0,+,-,-,-,-,-,+,-]
// use DP
// update currentNegativeSequence, currentPositiveSequence
// update globalNegativeSequence, globalPositiveSequence

class Solution {
public:
  int getMaxLen(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    int cns = 0, cps = 0, gns = 0, gps = 0;
    // initial state
    for (int i = 0; i<nums.size(); ++i) {
      if (nums[i] == 0) {
        cns = 0;
        cps = 0;
      } else if (nums[i] > 0) {
        cps += 1;
        cns = (cns == 0) ? 0 : cns+1;
      } else {
        int tmp = (cns == 0) ? 0 : cns+1;
        cns = max(cps+1, 1);
        cps = tmp;
      }
      // cout << cps << " . " << cns << endl;
      gns = max(gns, cns);
      gps = max(gps, cps);
    }
    return gps;
  }
};

int main() {
  vector<int> test1 = {1,-2,-3,4,1,-2,-3,4};
  vector<int> test2 = {0,1,-2,-3,-4};
  vector<int> test3 = {-1,-2,-3,0,1};
  cout << Solution().getMaxLen(test1) << endl;
  cout << Solution().getMaxLen(test2) << endl;
  cout << Solution().getMaxLen(test3) << endl;
}