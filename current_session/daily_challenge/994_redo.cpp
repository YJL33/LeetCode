// clang++ -std=c++17 c++/994_redo.cpp -o 994 && ./994 -v
// clang++ -std=c++17 daily_challenge/994_redo.cpp -o 994 && ./994 -v
// count the number of fresh ones first
// BFS
#include <iostream>
#include <vector>
#include <deque>
#include <set>

using namespace std;

class Solution {
public:
  int orangesRotting(vector<vector<int>>& grid) {
    deque<vector<int>> dq;
    int freshCount = 0;
    int H = grid.size(), W = grid[0].size();

    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
        if (grid[i][j] == 1) {
          freshCount++;
        } else if (grid[i][j] == 2) {
          dq.push_back(vector<int>{0, i, j});
        }
      }
    }

    set<pair<int,int>> seen;
    int needed = 0;

    while (dq.size() != 0) {
      vector<int> v = dq[0];
      dq.pop_front();
      int r = v[1], c = v[2], day = v[0];     // at day, here's a rotten one
      cout << r << " , " << c << " , " << day << endl;
      if (seen.find(pair<int,int>{r,c}) != seen.end()) continue;
      seen.insert(pair<int,int>{r,c});

      needed = max(needed, day);
      if (grid[r][c] == 1) freshCount -= 1;   // 0:given rotten 1:become rotten
      grid[r][c] = 2;

      vector<vector<int>> nbs;
      nbs.push_back(vector<int>{r+1,c});
      nbs.push_back(vector<int>{r-1,c});
      nbs.push_back(vector<int>{r,c+1});
      nbs.push_back(vector<int>{r,c-1});
      for (auto nb: nbs) {
        if (inBoundary(nb[0], nb[1], H, W) && grid[nb[0]][nb[1]] == 1) {
          dq.push_back(vector<int>{day+1, nb[0], nb[1]});
        }
      }
      
    }

    // cout << freshCount << " . " << needed << endl;

    return (freshCount == 0) ? needed : -1;
  }

  bool inBoundary(int i, int j, int H, int W) {
    return (0 <= i && i < H && 0 <= j && j < W);
  }
};

int main() {
  vector<vector<int>> test1 = {{2,1,1},{1,1,0},{0,1,1}};
  vector<vector<int>> test2 = {{2,1,1},{0,1,1},{1,0,1}};
  vector<vector<int>> test3 = {{0,2}};
  vector<vector<int>> test4 = {{2,2},{1,1},{0,0},{2,0}};
  // cout << Solution().orangesRotting(test1) << endl;
  // cout << Solution().orangesRotting(test2) << endl;
  // cout << Solution().orangesRotting(test3) << endl;
  cout << Solution().orangesRotting(test4) << endl;
}