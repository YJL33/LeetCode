#include <iostream>
#include <vector>

using namespace std;

// clang++ -std=c++17 c++/718.cpp -o 718 && ./718 -v
// analysis: naive approach (try each i, j => compare => O(n^3))
// say given A, B, for each a in A, if some b in B that satisfied a == b: check longest repeated array
// find next unique a that outside of current max substring

// use DP
// dp[i][j] == solution of A[:i] and B[:j]
// time analysis: O(M*N)

class Solution {
public:
  int findLength(vector<int>& nums1, vector<int>& nums2) {
    vector<vector<int>> dp(nums1.size()+1, vector<int>(nums2.size()+1, 0));
    int maxLen = 0;
    for (int i = 1; i <= nums1.size(); ++i) {
      for (int j = 1; j <= nums2.size(); ++j) {
        if (nums1[i-1] == nums2[j-1]) {
          dp[i][j] = 1+dp[i-1][j-1];
          maxLen = max(maxLen , dp[i][j]);
        }
      }
    }
    return maxLen;
  }
};

int main() {
  vector<int> test1a = {1,2,3,2,1};
  vector<int> test1b = {3,2,1,4,7};
  vector<int> test2a = {0,0,0,0,0};
  vector<int> test2b = {0,0,0,0,0};
  vector<int> test3a = {1,1,0,1,1,0,0,0,0,0};
  vector<int> test3b = {1,0,1,0,0,0,0,0,1,1};

  cout << Solution().findLength(test1a, test1b) << " == 3" << endl;
  cout << Solution().findLength(test2a, test2b) << " == 5" << endl;
  cout << Solution().findLength(test3a, test3b) << " == 6" << endl;
}