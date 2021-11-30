#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
    int H = obstacleGrid.size(), W = obstacleGrid[0].size();
    if (obstacleGrid[0][0] == 1 or obstacleGrid[H-1][W-1] == 1) return 0;

    // use an 2D array => DP
    vector<vector<int>> dp(H, vector<int>(W, 0));
    dp[0][0] = 1;

    for (int i=0; i < H; ++i) {
      for (int j=0; j < W; ++j) {
        if (obstacleGrid[i][j] == 0) {
          int add = 0;
          if (i-1 >= 0 && j >= 0) add += dp[i-1][j];
          if (i >= 0 && j-1 >= 0) add += dp[i][j-1];
          dp[i][j] += add;
        }
      }
    }

    return dp[H-1][W-1];
  }
};

int main() {
  cout << Solution().uniquePathsWithObstacles() << endl;
}