#include <iostream>
#include <vector>

using namespace std;

// use 2 Vectors (arrays)
// analysis: O(n) where n = length of nums

class Solution {
public:
  int partitionDisjoint(vector<int>& nums) {
    // get max value
    int maxVal = nums[0];
    for (int i = 1; i < nums.size(); ++i) {
      maxVal = max(maxVal, nums[i]);
    }
    int L = nums.size();
    vector<int> rightMin(L, nums[L-1]);
    // get right min array
    for (int i = L-2; i >= 0; --i) {
      rightMin[i] = min(rightMin[i+1], nums[i]);
    }

    vector<int> leftMax(L, nums[0]);
    // update left max array while checking the partition
    // partition start at nums[:i], nums[i:]
    for (int i = 1; i < nums.size(); ++i) {
      leftMax[i] = max(leftMax[i-1], nums[i]);
      // ending criteria
      if (leftMax[i-1] <= rightMin[i]) {
        return i;
      }
    }
    // cout << "???" << endl;
    return L;
  }
};

int main() {
  vector<int> test = {5,0,3,8,6};
  vector<int> test2 = {1,1,1,0,6,12};
  cout << Solution().partitionDisjoint(test) << " == 3" << endl;
  cout << Solution().partitionDisjoint(test2) << " == 4" << endl;
}