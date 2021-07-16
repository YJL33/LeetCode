#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maximumScore(vector<int>& nums, int k) {
    long maxScore = long(nums[k]);
    long minScore = long(nums[k]);
    int l = k, r = k;
    while (l>0 || r<nums.size()-1) {
      if (l==0 || (nums[l-1] < nums[r+1])) {
        minScore = min(minScore, long(nums[++r]));
      }
      else {
        minScore = min(minScore, long(nums[--l])) ;
      }
      maxScore = max(maxScore, minScore*(r-l+1));
    }
    return maxScore;
  }
};