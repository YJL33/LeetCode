#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> permute(vector<int>& nums) {
    vector<vector<int> > res;
    if (nums.size() == 1) {
        res.push_back(nums);
        return res;
    }
    for (int i=0; i<nums.size(); ++i) {
      swap(nums[i], nums[nums.size()-1]);
      int x = nums[nums.size()-1];
      nums.pop_back();
      vector<vector<int> > tmp = permute(nums);
      nums.push_back(x);
      swap(nums[i], nums[nums.size()-1]);
      for (auto sol:tmp) {
        sol.push_back(x);
        res.push_back(sol);
      }
      // res.push_back(tmp);
    }
    return res;
  }
};