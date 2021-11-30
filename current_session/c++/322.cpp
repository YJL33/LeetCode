#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int coinChange(vector<int>& coins, int amount) {
    if (amount == 0) return 0;
    // use DP
    int dp[amount+1];
    dp[0] = 0;
    // sorting
    sort(begin(coins), end(coins));
    for (int a=1; a<=amount; ++a) {
      // can only use coins that smaller than a
      dp[a] = INT_MAX;
      for (int j=0; j<coins.size(); ++j) {
        if (coins[j] > a) {
          break;
        }
        if (dp[a-coins[j]] != INT_MAX) {
          dp[a] = min({dp[a], 1+dp[a-coins[j]]});
        }
      }
    }

    if (dp[amount] == INT_MAX) {
      return -1;
    }
    else {
      return dp[amount];
    }
  }
};

int main() {
  vector<int>test1 = {1,2,5};
  vector<int>test2 = {2};
  vector<int>test3 = {1};
  vector<int>test4 = {1};
  vector<int>test5 = {1};
  vector<int>test6 = {474,83,404,3};
  cout << Solution().coinChange(test1, 11) << endl;
  cout << Solution().coinChange(test2, 1) << endl;
  cout << Solution().coinChange(test3, 0) << endl;
  cout << Solution().coinChange(test4, 1) << endl;
  cout << Solution().coinChange(test5, 2) << endl;
  cout << Solution().coinChange(test6, 264) << endl;

}