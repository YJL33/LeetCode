#include <iostream>
#include <vector>
#include <set>

using namespace std;

// use backtrack
// skip duplicate only if it's not start
class Solution {
public:
  vector<vector<int>> ans;
  vector<vector<int>> subsetsWithDup(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    helper(nums, vector<int>{}, 0);
    return ans;
  }
  void helper(vector<int>& arr, vector<int> tmp, int start) {
    ans.push_back(tmp);
    for (int i=start; i<arr.size(); ++i) {
      if(i > start && arr[i] == arr[i-1]) continue; // skip duplicates
      tmp.push_back(arr[i]);
      helper(arr, tmp, i+1);
      tmp.pop_back();
    }
  }
};