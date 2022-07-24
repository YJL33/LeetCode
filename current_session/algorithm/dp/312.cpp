#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxCoins(vector<int>& nums) {
    // use DP
    // dp[i][j] is the solution of nums[i:j+1]
    // return dp[0][-1]
    vector<int> arr;

    arr.push_back(1);
    for (auto n : nums) {
      arr.push_back(n);
    }
    arr.push_back(1);

    int L = arr.size();
    vector<vector<int> > dp(L, vector<int>(L, 0));

    for (int i=L-2; i>=0; --i) {
      for (int j=i+2; j<L; ++j) {
        for (int k=i+1; k<j; ++k) {
          dp[i][j] = max(dp[i][j], arr[i]*arr[k]*arr[j]+dp[i][k]+dp[k][j]);
        }
      }
    }
    return dp[0][L-1];
  }
};


// cp dp/312.cpp dp/sol.cpp && clang++ -std=c++17 dp/sol.cpp -o sol && ./sol -v 
int main() {
  vector<int>test1 = {3,1,5,8};
  cout << Solution().maxCoins(test1) << " should be 167"<< endl;
}