/*
 * @lc app=leetcode id=1260 lang=cpp
 *
 * [1260] Shift 2D Grid
 */

// @lc code=start
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
    // simply create a new vector and then push the numbers in order
    // TC: O(m*n)
    // SC: O(m*n)
    int h = grid.size(), w = grid[0].size();
    int L = h*w;
    if (k%L == 0) return grid;

    vector<vector<int>> arr;
    for (int i = 0; i < h; i++) {
      vector<int> row = vector<int>(w);
      arr.push_back(row);
    }

    int cur = L-k%L;
    for (int i = 0; i < L; i++) {
      int h1 = i/w, r1 = i%w;
      int h2 = cur/w, r2 = cur%w;
      arr[h1][r1] = grid[h2][r2];
      cur = ++cur%L;
    }
    return arr;
  }
};
// @lc code=end

