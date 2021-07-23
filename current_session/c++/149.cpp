#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <limits>

using namespace std;

// ax+by=c
// y1 = slope*x1 + intercept
// y2 = slope*x2 + intercept
// naive approach: try all i j in points
// use a map to store slope and intersection
// key:{slope,intersect}, val:set of points
// time complexity: O(n^2)

class Solution {
public:
  int maxPoints(vector<vector<int>>& points) {
    if (points.size() <= 2) return points.size();
    int maxCnt = 0;
    map<pair<float, float>, set<int>> lineMap;
    for (int i=0; i<points.size(); ++i) {
      float x1 = points[i][0], y1 = points[i][1];
      for (int j=i+1; j<points.size(); ++j) {
        pair<float, float> line = getLine(x1, y1, points[j][0],points[j][1]);
        if (lineMap.find(line) == lineMap.end()) {
          set<int> duo{i,j};
          lineMap.insert(pair<pair<float, float>,set<int>>{line, duo});
        } else {
          // lineMap[line].insert(i);
          lineMap[line].insert(j);
        }
        int curSize = lineMap[line].size();
        maxCnt = max(maxCnt, curSize);
      }
    }
    return maxCnt;
  }
private:
  pair<float, float> getLine(float x1, float y1, float x2, float y2) {
    // edge case: vertical lines
    if (x1==x2) return pair<float, float>{x1, numeric_limits<float>::max()};
    // normal cases
    float dx = x2-x1, dy = y2-y1;
    float slope = dy/dx;
    float intercept = y1-slope*x1;
    return pair<float, float>{slope, intercept};
  }
};
int main() {
  int n;  // number of points
  cin >> n;
  vector<vector<int>> points;
  while (n>0) {
    int x, y;
    cin >> x;
    cin >> y;
    points.push_back(vector<int>{x,y});
    --n;
  }
  cout << "max points:" << Solution().maxPoints(points) << endl;
}