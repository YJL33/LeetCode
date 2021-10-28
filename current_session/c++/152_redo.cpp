#include <iostream>
#include <vector>

using namespace std;

// clang++ -std=c++17 c++/152_redo.cpp -o 152 && ./152 -v
class Solution {
public:
  int maxProduct(vector<int>& nums) {
    if (nums.size() == 0) return 0;
    int localMax = nums[0], localMin = nums[0], globalMax = nums[0];
    for (int i = 1; i < nums.size(); ++i) {
      int tmpMax = max(nums[i]*localMax, nums[i]*localMin);
      int tmpMin = min(nums[i]*localMax, nums[i]*localMin);
      localMax = max(nums[i], tmpMax);
      localMin = min(nums[i], tmpMin);
      globalMax = max(globalMax, localMax);
      // cout << "localMax: " << localMax << endl;
      // cout << "localMin: " << localMin << endl;
    }
    return globalMax;
  }
};

int main() {
  vector<int> test1 = {2,3,-2,4};
  vector<int> test2 = {-2,0,-1};
  vector<int> test3 = {-2};
  vector<int> test4 = {-4,-3,-2};
  cout << Solution().maxProduct(test1) << endl;
  cout << Solution().maxProduct(test2) << endl;
  cout << Solution().maxProduct(test3) << endl;
  cout << Solution().maxProduct(test4) << endl;
}