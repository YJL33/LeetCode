#include <iostream>
#include <vector>
#include <set>

using namespace std;

class Solution {
public:
  int longestConsecutive(vector<int>& nums) {
    set<int> numSet;
    for (int i=0;i<nums.size();++i) {
      numSet.insert(nums[i]);
    }
    int maxLen = 0;
    for (auto n:nums) {
      if (numSet.find(n) != numSet.end()) {
        int l=n, r=n+1;
        while (numSet.find(l) != numSet.end()) {
          numSet.erase(l);
          l--;
        }
        while (numSet.find(r) != numSet.end()) {
          numSet.erase(r);
          r++;
        }
        maxLen = max(maxLen, r-l-1);
      }
    }
    return maxLen;
  }
};