#include <iostream>
#include <vector>
#include <queue>

using namespace std;
// use bfs
// use visited
class Solution {
public:
  int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
    int H = grid.size(), W = grid[0].size();
    queue<vector<int>> q;
    if (grid[0][0] == 1 || grid.back().back() == 1) return -1;
    q.push({0,0,1});
    while (!q.empty()) {
      vector<int> p = q.front();
      q.pop();
      int i = p[0], j=p[1], cnt=p[2];
      if (i==H-1 && j==W-1) return cnt;
      helper(grid, q, i+1, j+1, cnt, H, W);
      helper(grid, q, i+1, j, cnt, H, W);
      helper(grid, q, i+1, j-1, cnt, H, W);
      helper(grid, q, i, j+1, cnt, H, W);
      helper(grid, q, i, j-1, cnt, H, W);
      helper(grid, q, i-1, j+1, cnt, H, W);
      helper(grid, q, i-1, j, cnt, H, W);
      helper(grid, q, i-1, j-1, cnt, H, W);
    }
    return -1;
  }
  void helper(vector<vector<int>>& grid, queue<vector<int>> &nbs, int a, int b, int c, int H, int W) {
    if (0 <= a && a < H && 0 <= b && b < W && grid[a][b] == 0) {
      // cout << "a:" << a << "  b:" << b << endl;
      nbs.push(vector<int>{a,b,c+1});
      grid[a][b] = 1;
    }
  }
};