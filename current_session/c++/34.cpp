#include <vector>
#include <iostream>

using namespace std;


// simply binary search first and last position
// its like python's bisect_left and bisect_right
class Solution {
public:
  vector<int> searchRange(vector<int>& nums, int target) {
    if (nums.size()==0 || target>nums[nums.size()-1] || target<nums[0]) {
      return vector<int>{-1,-1};
    }
    int l = bisect(nums, target, true);
    if (nums[l] != target || l==-1) return vector<int>{-1,-1};
    int r = bisect(nums, target, false);
    if (nums[r] != target) --r;
    return vector<int>{l,r};
  }
private:
  int bisect(vector<int>& nums, int target, bool isLeft) {
    int l = 0, r = nums.size()-1;
    while (l < r) {
      int m=l+(r-l)/2;
      if (nums[m] == target) {          // bisect_left or bisect_right
        if (isLeft) r=m;
        else l=m+1;
      } else if (nums[m] > target) {    // at left side
        r=m;
      } else {                          // at right side
        l=m+1;
      }
    }
    return l;
  }
  
};