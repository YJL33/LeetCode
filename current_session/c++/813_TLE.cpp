#include <iostream>
#include <vector>
#include <map>
#include <numeric>

using namespace std;

// score: avg of each subsum
// return max score of partitions among all possible partitions
// naive approach: try all sub sum, time complexity O(n^2)
// use dfs and memorization

class Solution {
public:
  map<pair<int, int>, double> avgmap;
  map<pair<int, int>, double> solmap;
  double largestSumOfAverages(vector<int>& nums, int k) {
    if (k==1) return double(accumulate(nums.begin(), nums.end(), 0))/nums.size();
    createAvgMap(nums);
    // use solution map to store partial sol
    return dfs(0, k, nums, nums.size());
  }
private:
  void createAvgMap(vector<int>& nums) {
    // create avg map
    for (int i=0; i<nums.size(); ++i) {
      int localSum = nums[i];
      for (int j=i+1; j<=nums.size(); ++j) {
        pair<int,int>x = {i,j};
        avgmap[x] = double(localSum)/(j-i);
        // cout << "first:" << i << j << " second:" << double(localSum)/(j-i)<< endl;
        if (j<nums.size()) localSum += nums[j];
      }
    }
    return;
  }
  double dfs(int start, int k, vector<int>& arr, int arrLen) {
    if (start>=arrLen || k == 0) return double(-1);
    pair<int,int> inputPair = {start, arrLen};
    if (k == 1) return avgmap[inputPair];
    if (solmap.find(inputPair) != solmap.end()) return solmap[inputPair];
    if (k == arrLen-start) {
        // cout << "start:" << start << "  k:" << k << "  partialsum: " << accumulate(arr.begin()+start, arr.end(), 0) << endl;
        solmap[inputPair] = double(accumulate(arr.begin()+start, arr.end(), 0));
        return solmap[inputPair];
    }
    double sol = 0;
    for (int j=start+1; j<=arrLen; ++j) {
      pair<int,int> p = {start, j};
      sol = max(sol, avgmap[p]+dfs(j, k-1, arr, arrLen));
    }
    return sol;
  }
};