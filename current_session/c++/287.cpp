#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
  int findDuplicate(vector<int>& nums) {
    int currentSum = accumulate(nums.begin(), nums.end(),0);
    int shouldbe = (nums.size()-1)*(nums.size())/2;
    return currentSum-shouldbe;
  }
};