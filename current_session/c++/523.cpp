#include <iostream>
#include <vector>
#include <map>

using namespace std;

// leverage partial sum
// first, we create an array where arr[i] = sum(arr[:i+1])
// then use a dict to store the mod value, if exist (and length is correct)
// then return true
class Solution {
public:
  bool checkSubarraySum(vector<int>& nums, int k) {
    // create array
    vector<int> lsum;
    int prev = 0;
    for (auto n: nums) {
      prev = prev+n;
      lsum.push_back(prev);
    }

    map<int, int> modMap;
    modMap.insert({0, -1});

    // go through nums again
    for (int i=0; i<lsum.size(); ++i) {
      int x = lsum[i];
      if (modMap.empty()) {
        modMap.insert({lsum[i]%k, i});
      } else {
        // check if its counter part exists
        int y = x%k;
        if (modMap.find(y) != modMap.end() && i-modMap[y] > 1) {
          return true;
        } else {
          modMap.insert({y, i});
        }
      }
    }
    return false;
  }
};
