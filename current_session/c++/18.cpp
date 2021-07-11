#include <iostream>
#include <vector>
#include <numeric>
#include <set>
#include <map>
#include <sstream>

using namespace std;

// leverage 3Sum and 2Sum
// sort first
// O(nlogn)*O(n)*O(n)
class Solution {
public:
  vector<vector<int>> fourSum(vector<int>& nums, int target) {
    if (nums.size() < 4) return res;
    if (nums.size() == 4 && accumulate(nums.begin(), nums.end(),0) != target) return res;
    sort(nums.begin(), nums.end());

    // trim
    if (nums.at(nums.size()-1)+nums.at(nums.size()-2)+nums.at(nums.size()-3)+nums.at(nums.size()-4)<target) return res;
    if (nums.at(1)+nums.at(2)+nums.at(3)+nums.at(0)>target) return res;
    vector<int>carry;
    for (int i=0; i<nums.size(); ++i) {
      carry.push_back(nums[i]);
      threeSum(nums, i+1, target-nums[i], carry);    // threeSum
      carry.pop_back();
    }
    return res;
  }
private:
  vector<vector<int> > res;
  set<vector<int> > seenSolSet;
  void threeSum(vector<int>& nums, int nextI, int threeSumTarget, vector<int> carry) {
    if (nums.size()-nextI < 3) return;
    // trim
    if (nums.at(nums.size()-1)+nums.at(nums.size()-2)+nums.at(nums.size()-3)<threeSumTarget) return;
    if (nums.at(nextI)+nums.at(nextI+1)+nums.at(nextI+2)>threeSumTarget) return;

    for (int i=nextI; i<nums.size(); ++i) {
      carry.push_back(nums[i]);
      twoSum(nums, i+1, threeSumTarget-nums[i], carry);    // twoSum
      carry.pop_back();
    }
    return;
  }
  void twoSum(vector<int>& nums, int nextI, int twoSumTarget, vector<int> carry) {
    if (nums.size()-nextI < 2) return;
    // trim
    if (nums.at(nums.size()-1)+nums.at(nums.size()-2)<twoSumTarget) return;
    if (nums.at(nextI)+nums.at(nextI+1)>twoSumTarget) return;

    // use a map to store seen values, and check target-i is in the map or not
    map<int, int>seen;
    for (int i=nextI; i<nums.size(); ++i) {
      if (seen.find(twoSumTarget - nums.at(i)) == seen.end() ) {
        seen[nums.at(i)] = i;
      } else {
        vector<int> sol{nums.at(i),twoSumTarget-nums.at(i),carry.at(0),carry.at(1)};
        sort(sol.begin(), sol.end());
        if (seenSolSet.find(sol) == seenSolSet.end()) {
          seenSolSet.insert(sol);
          res.push_back(sol);
        };
      }
    }
    return;
  }
};