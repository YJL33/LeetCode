#include <iostream>
#include <vector>
#include <map>

using namespace std;

class SparseVector {
public:
  map<int,int> mp;
  int size;
  SparseVector(vector<int> &nums) {
    for (int i=0; i<nums.size();i++) {
      if (nums[i]!=0) mp[i] = nums[i];
    }
    size = nums.size();
  }

  // Return the dotProduct of two sparse vectors
  int dotProduct(SparseVector& vec) {
    int res=0;
    for (int i=0; i<size; i++) {
      if (mp.find(i) != mp.end() && vec.mp.find(i) != vec.mp.end()) res += mp[i]*vec.mp[i];
    }
    return res;
  }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);