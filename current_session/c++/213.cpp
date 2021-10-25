// clang++ -std=c++17 c++/213.cpp -o 213 && ./213 -v
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int rob(vector<int>& nums) {
    // use DP
    // remove the minimum house then treat it as linear one
    if (nums.size() == 1) {return nums[0];}
    int L = nums.size();
    return max(finder(0, L-1, nums), finder(1, L, nums));
  }

  // search from start to end-1
  int finder(int start, int end, vector<int>& nums) {
    int rob = 0, notRob = 0;
    for (int j = start; j < end; ++j) {
      int tmp = notRob + nums[j];
      notRob = max(notRob, rob);
      rob = tmp;
    }
    return max(rob, notRob);
  }
};

int main() {
  vector<int> test1 = {2,3,2};
  vector<int> test2 = {1,7,9,2};
  vector<int> test3 = {1,2,3,1};
  cout << Solution().rob(test1) << endl;
  cout << Solution().rob(test2) << endl;
  cout << Solution().rob(test3) << endl;
}