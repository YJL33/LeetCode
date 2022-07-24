#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
  int longestPalindromeSubseq(string s) {
    // use DP
    int N = s.size();
    vector<vector<int>> dp(N, vector<int>(N, 0));
    for (int i=N-1; i>=0; --i) {
      for (int j=i; j<N; ++j) {
        if (i == j) {
          dp[i][j] = 1;
        } else if (s[i] == s[j]) {
          dp[i][j] = dp[i+1][j-1] + 2;
        } else {
          dp[i][j] = max(dp[i][j-1], dp[i+1][j]);
        }
      }
    }
    return dp[0][N-1];
  }
};

// cp dp/516.cpp dp/sol.cpp && clang++ -std=c++17 dp/sol.cpp -o sol && ./sol -v 
int main() {
  string test1 = "bbbab";
  string test2 = "cbbd";
  cout << Solution().longestPalindromeSubseq(test1) << " should be 4"<< endl;
  cout << Solution().longestPalindromeSubseq(test2) << " should be 2"<< endl;
}