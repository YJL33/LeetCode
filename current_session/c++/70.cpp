#include <iostream>
#include <vector>

using namespace std;

// use dp
// dp[i] is the solution at n=i, where
// dp[i] = dp[i-1] + dp[i-2]
class Solution {
 public:
  int climbStairs(int n) {
    if (n <= 3) return n;
    int dp = 3, prev = 2, i = 3;
    while (i < n) {int tmp=dp; dp=dp+prev; prev=tmp; i++;}
    return dp;
  }
};