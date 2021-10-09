#include <iostream>
#include <vector>

using namespace std;

// clang++ -std=c++17 c++/1504.cpp -o 1504 && ./1504 -v
// use histograms
// 
class Solution {
public:
  int numSubmat(vector<vector<int>>& mat) {
    int H = mat.size(); 
    int W = mat[0].size();
    // tweak the mat
    for (int i = 0; i < H; ++i) {
      for (int j = 0; j < W; ++j) {
        if (mat[i][j] != 0 && i-1 >= 0) {
          mat[i][j] += mat[i-1][j];
        } 
      }
    }
    
    // check the tweak
    // for (auto r: mat) {
    //   for (int i = 0; i < r.size(); ++i) {cout << r[i];}
    //   cout << endl;
    // }

    // handle the histogram
    int ans = 0;
    for (int i = 0; i < H; ++i) {
      vector<int> mStack;
      int tmp = 0;
      for (int j = 0; j < W; ++j) {
        while (mStack.size() > 0 && mat[i][mStack.back()] > mat[i][j]) {
          int jj = mStack.back();
          mStack.pop_back();
          int kk = mStack.size() > 0 ? mStack.back() : -1;
          tmp -= (mat[i][jj] - mat[i][j])*(jj - kk);
        }
        tmp += mat[i][j];
        ans += tmp;
        mStack.push_back(j);
      }
    }

    return ans;
  }
};

int main() {
  vector<vector<int>> test = {{1,1,0},{0,1,1},{1,1,1}};
  vector<vector<int>> test2 = {{1,1,1},{0,1,0},{1,0,1}};
  vector<vector<int>> test3 = {{1,1,1},{0,1,1},{1,0,1}};
  vector<vector<int>> test4 = {{1,1,1,1,0},{1,0,0,1,0},{0,0,1,0,1},{0,1,0,0,0}};
  // print(Solution().numSubmat([[1,1,0],[0,1,1],[1,1,1]]), 'sb 17')
  cout << Solution().numSubmat(test) << " should be 17" << endl;
  cout << Solution().numSubmat(test2) << " should be 10" << endl;
  cout << Solution().numSubmat(test3) << " should be 16" << endl;
  cout << Solution().numSubmat(test4) << " should be 17" << endl;
}