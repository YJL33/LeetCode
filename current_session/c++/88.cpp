#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
    if (n==0) return;
    if (m==0) {
      for (int i=0; i<nums1.size(); ++i) nums1[i] = nums2[i];
      return;
    }
    int p1 = m-1;
    int p2 = n-1;
    int x = m+n-1;
    while (p2>=0 || p1>=0) {
      if (p2<0) {
        break;
      } else if (p1>=0 && p2>=0 && nums1[p1] >= nums2[p2]) {
        nums1[x] = nums1[p1];
        --x;
        --p1;
      } else {
        nums1[x] = nums2[p2];
        --x;
        --p2;
      } 
    }
    return;
  }
};