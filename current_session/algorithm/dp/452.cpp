#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int findMinArrowShots(vector<vector<int>>& points) {
    // similar as 435, handle overlap carefully
    if(points.size() == 1) return 1;
    sort(points.begin(), points.end());
    int prev_start = points[0][0], prev_end = points[0][1], cnt = 1;
    for (int i = 1; i < points.size(); ++i) {
      int start = points[i][0], end = points[i][1];
      if (start <= prev_end && prev_start <= end) {   // overlap
        if (end < prev_end) {
          prev_end = end;
        }
      } else {
        prev_start = start, prev_end = end;
        cnt++;
      }
    }
    return cnt;
  }
};

// cp dp/452.cpp dp/sol.cpp && clang++ -std=c++17 dp/sol.cpp -o sol && ./sol -v 
int main() {
  vector<vector<int>> test1 = {{10,16},{2,8},{1,6},{7,12}};
  vector<vector<int>> test2 = {{1,2},{3,4},{5,6},{7,8}};
  vector<vector<int>> test3 = {{1,2},{3,4},{2,3},{4,5}};
  cout << Solution().findMinArrowShots(test1) << " should be 2"<< endl;
  cout << Solution().findMinArrowShots(test2) << " should be 4"<< endl;
  cout << Solution().findMinArrowShots(test3) << " should be 2"<< endl;
}