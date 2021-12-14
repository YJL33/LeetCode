#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxSumAfterOperation(vector<int>& nums) {
    // use DP
    int localSumWithNoSq = nums[0];
    int localSumWithSq = nums[0]*nums[0];
    int globalSum = max(localSumWithSq, localSumWithNoSq);

    for (int i=1; i<nums.size(); ++i) {
      int x = nums[i]*nums[i];
      localSumWithSq = max({x, localSumWithNoSq+x, localSumWithSq+nums[i]});
      localSumWithNoSq = max(localSumWithNoSq+nums[i], nums[i]);
      globalSum = max({globalSum, localSumWithSq, localSumWithNoSq});
    }
    return globalSum;
  }
};


// clang++ -std=c++17 c++/1746.cpp -o 1746 && ./1746 -v
int main() {
  vector<int> test1 = {2,-1,-4,-3};
  vector<int> test2 = {1,-1,1,1,-1,-1,1};
  cout << Solution().maxSumAfterOperation(test1) << endl;
  cout << Solution().maxSumAfterOperation(test2) << endl;
}