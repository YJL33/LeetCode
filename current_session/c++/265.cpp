#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int minCostII(vector<vector<int>>& costs) {
    int n = costs.size();
    if (n==0) return 0;
    int k = costs[0].size();
    if (k==1) return costs[0][0];

    vector<int> dp(k, 0);
    int min1, min2;

    for(int i=0; i<n; ++i){
      int min1_old = (i==0) ? 0 : min1;
      int min2_old = (i==0) ? 0 : min2;
      min1 = INT_MAX;
      min2 = INT_MAX;
      for(int j=0; j<k; ++j){
        if (dp[j] != min1_old || min1_old == min2_old) {
          dp[j] = min1_old + costs[i][j];
        } else {
          dp[j] = min2_old + costs[i][j];
        }

        if (min1 <= dp[j]) {
          min2 = min(min2, dp[j]);
        } else {
          min2 = min1;
          min1 = dp[j];
        }
      }
    }
    return min1;
  }
};

int main() {
  vector<int> c1 = {20,19,11,13,12,16,16,17,15,9,5,18};
  vector<int> c2 = {3,8,15,17,19,8,18,3,11,6,7,12};
  vector<int> c3 = {15,4,11,1,18,2,10,9,3,6,4,15};
  vector<vector<int>> costs;
  costs.push_back(c1);
  costs.push_back(c2);
  costs.push_back(c3);
  cout << Solution().minCostII(costs) << endl;
}