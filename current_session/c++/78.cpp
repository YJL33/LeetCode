#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> res;
  vector<vector<int>> subsets(vector<int>& nums) {
    helper(nums, vector<int>{}, 0);
    return res;
  }
  void helper(vector<int>& nums, vector<int> tmp, int start) {
    res.push_back(tmp);
    for (int i=start; i<nums.size(); ++i) {
      tmp.push_back(nums[i]);
      helper(nums, tmp, i+1);
      tmp.pop_back();
    }
  }
};