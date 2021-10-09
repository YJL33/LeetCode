#include <iostream>
#include <vector>

using namespace std;

// use DP(?)
// DP[i][j] = min distance of w1[:i+1] and w2[:j+1]
// we can use: insert/delete/replace
// if w1[i] == w2[j] => same as dp[i-1][j-1]
// else (e.g. hor, hoa) => min from:
//          replace(dp[i-1][j-1]+1)
//          insert(dp[i][j-1]+1, dp[i-1][j]+1)

// e.g. w1 = horse, w2 = ros
//    0  1  2  3  4  5    w1
// 0  1
// 1
// 2
// 3
// w2

class Solution {
public:
  int minDistance(string word1, string word2) {
    if (word1.size() == 0 && word2.size() == 0) return 0;
    if (word1.size() == 0) return word2.size();
    if (word2.size() == 0) return word1.size();

    int A = word1.size(), B = word2.size();
    vector<vector<int>> dp(A+1, vector<int>(B+1, 0));
    for (int i = 0; i <= A; ++i) {
      for (int j = 0; j <= B; ++j) {
        if (i==0 && j==0) {
          dp[i][j] = 0;               // edge case
        } else if (i == 0) {
          dp[i][j] = dp[i][j-1]+1;    // insert/delete
        } else if (j == 0) {
          dp[i][j] = dp[i-1][j]+1;    // insert/delete
        } else if (word1[i-1] == word2[j-1]) {
          dp[i][j] = dp[i-1][j-1];    // as same as (w1[i-2], w2[j-2])
        } else {
          dp[i][j] = min({dp[i-1][j-1], dp[i-1][j], dp[i][j-1]})+1; // min from replace, insert
        }
      }
    }
    return dp[A][B];
  }
  
};

// clang++ -std=c++17 c++/72.cpp -o 72 && ./72 -v
int main() {
  cout << Solution().minDistance("horse", "ros") << endl;
  cout << Solution().minDistance("intention", "execution") << endl;
  cout << Solution().minDistance("sea", "eat") << endl;
}