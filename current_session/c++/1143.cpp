#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int longestCommonSubsequence(string text1, string text2) {
    // use DP
    // dp[i][j] = ans of text1[:i] and text2[:j]
    // if text1[i] == text2[j]: dp[i][j] = dp[i-1][j-1] + 1
    int M = text1.size();
    int N = text2.size();
    vector<vector<int>> dp(M+1, vector<int>(N+1, 0));
    for (int i=0; i<M; ++i) {
      for (int j=0; j<N; ++j) {
        if (text1[i] == text2[j]) {
          dp[i+1][j+1] = dp[i][j]+1;
        } else {
          dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j]);
        }
      }
    }
    return dp[M][N];
  }
};

int main() {
  cout << Solution().longestCommonSubsequence("abcde", "ace") << endl;
}