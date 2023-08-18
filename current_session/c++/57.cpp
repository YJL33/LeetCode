#include <iostream>
#include <vector>

using namespace std;

// cp c++/57.cpp c++/sol.cpp && clang++ -std=c++17 c++/sol.cpp -o sol && ./sol -v 
class Solution {
public:
  vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
    vector<vector<int>> to_merge;
    vector<vector<int>> before;
    vector<vector<int>> after;
    for (auto i : intervals) {
      int s = i[0], e = i[1];
      if (e < newInterval[0]) {
        before.push_back(i);
      } else if (s > newInterval[1]) {
        after.push_back(i);
      } else {
        to_merge.push_back(i);
      }
    }
    int ns = newInterval[0], ne = newInterval[1];
    for (auto x : to_merge) {
      ns = min(x[0], ns);
      ne = max(x[1], ne);
    }
    before.push_back(vector<int>{ns, ne});
    before.insert(before.end(), after.begin(), after.end());
    return before;
  }
};

// cp c++/57.cpp c++/sol.cpp && clang++ -std=c++17 c++/sol.cpp -o sol && ./sol -v 
int main() {
  vector<vector<int>> interval1 = {{1,3},{6,9}};
  vector<int> new1 = {2,5};
  vector<vector<int>> interval2 = {{1,2},{3,5},{6,7},{8,10},{12,16}};
  vector<int> new2 = {4,8};
  vector<vector<int>> output1 = Solution().insert(interval1, new1);
  vector<vector<int>> output2 = Solution().insert(interval2, new2);
  cout << "output1: [";
  for (auto o : output1) {
    cout << "[" << o[0] << "," << o[1] << "]";
  }
  cout << "] should be [[1,5],[6,9]]" << endl;
  cout << "output2: [";
  for (auto o : output1) {
    cout << "[" << o[0] << "," << o[1] << "]";
  }
  cout << "] should be [[1,2],[3,10],[12,16]]"<< endl;
}