// clang++ -std=c++17 c++/740.cpp -o 740 && ./740 -v
#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
  int deleteAndEarn(vector<int>& nums) {
    // use DP
    // use map first
    map<int, int> numCnt;
    for (int i = 0; i < nums.size(); ++i) {
      if (numCnt.find(nums[i]) != numCnt.end()) {
        numCnt[nums[i]] += 1;
      } else {
        numCnt[nums[i]] = 1;
      }
    }

    // get all keys
    vector<int> uniqueNums;
    for (auto p : numCnt) {
      uniqueNums.push_back(p.first);
    }
    sort(uniqueNums.begin(), uniqueNums.end());

    // DP
    int use = 0, notUse = 0, last = -1;
    for (int i = 0; i < uniqueNums.size(); ++i) {
      int n = uniqueNums[i];
      int tmp = notUse + n*numCnt[n];
      // use freely
      if (last != -1 && n != last+1) {
        tmp = max(tmp, use+n*numCnt[n]);
      }
      notUse = max(use, notUse);
      use = tmp;
      last = n;
      // cout << "n: " << n << " cnt: " << numCnt[n] << " use: " << use << " notUse: " << notUse << endl;
    }

    return max(use, notUse);
  }
};

int main() {
  vector<int> test1 = {3,4,2};
  vector<int> test2 = {2,2,3,3,3,4};
  cout << Solution().deleteAndEarn(test1) <<  endl;
  cout << Solution().deleteAndEarn(test2) <<  endl;
}