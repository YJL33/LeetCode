#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// 1st pass: count the number of fresh
// 2nd pass: bfs, use queue of pair(i, j), and count the number of Rotten
// if n2<n1: return -1, else return day

class Solution {
public:
  int orangesRotting(vector<vector<int>>& grid) {
    int freshCount = 0;
    for (int i=0; i<grid.size(); ++i) {
      for (int j=0; j<grid[0].size(); ++j) {
        if (grid[i][j] == 1) {
          freshCount++;
        } else if (grid[i][j] == 2) {
          q.push({i,j});
        }
      }
    }
    if (freshCount == 0) return 0;

    int day = 0;
    while (!q.empty()) {
      int N = q.size();
      while (N--) {
        pair<int, int> rotPos = q.front();
        q.pop();
        int x = rotPos.first, y = rotPos.second;
        helper(x, y+1, grid);           // go 'infect' its 4 dirction neighbors
        helper(x, y-1, grid);
        helper(x+1, y, grid);
        helper(x-1, y, grid);
      }
      day += 1;
    }
    // cout<<"turn rotten"<<turnRotten<<endl;
    // cout<<"fresh Count"<<freshCount<<endl;
    if (turnRotten < freshCount) return -1;
    return max(0,day-1);
    
  }
private:
  int turnRotten = 0;
  queue<pair<int, int> > q;
  void helper(int x, int y, vector<vector<int>>& grid) {
    // only handle in bound and fresh
    // cout<<"x:"<<x<<"y:"<<y<<endl;
    if (0<=x && x<grid.size() && 0<=y && y<grid[0].size() && grid[x][y] == 1) {
      grid.at(x).at(y) = 2;
      turnRotten += 1;
      q.push({x,y});
    } 
    return;
  }
};

int main() {
  Solution sol = Solution();
  vector<vector<int> > g;
  vector<int> a{2,1,1};
  vector<int> b{1,1,0};
  vector<int> c{0,1,1};
  g.push_back(a);
  g.push_back(b);
  g.push_back(c);

  cout<<sol.orangesRotting(g)<<endl;

}