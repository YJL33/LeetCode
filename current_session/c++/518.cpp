#include <iostream>
#include <vector>

using namespace std;

// use DP
// dp[P+Q] += dp[Q] if there's a coin P
// we assign dp[0] = 1 (take no coins)
// start from edge cases
// coins: [2], amount: 6
// dp = [1,0,1,0,1,0,1]
// coins: [2,3], amount:6
// dp = [1,0,1,1,1,1,2]

class Solution {
public:
  int change(int amount, vector<int>& coins) {
    vector<int> dp(amount+1, 0);
    // sort(coins.begin(), coins.end());
    dp[0] = 1;
    for (auto c: coins) {
      for (int j=1; j<amount+1; ++j) {
        if (j >= c) {
          dp[j] += dp[j-c];
        }
      }
    }
    return dp[amount];
  }
};