#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> intervalIntersection(vector<vector<int>>& firstList, vector<vector<int>>& secondList) {
    vector<pair<int,int>> events;
    for (auto e:firstList) {
      events.push_back(pair<int,int>{e[0], 0});
      events.push_back(pair<int,int>{e[1], 1});
    }
    for (auto e:secondList) {
      events.push_back(pair<int,int>{e[0], 0});
      events.push_back(pair<int,int>{e[1], 1});
    }
    sort(events.begin(), events.end());
    int startCnt = 0;
    int startTime = INT_MAX;
    vector<vector<int>> res;
    for (auto x: events) {
      if (x.second%2 == 0) {
        startCnt += 1;
      } else {
        startCnt -= 1;
      }
      if (startCnt == 2) {
        startTime = x.first;
      } else if (startTime != INT_MAX) {
        res.push_back(vector<int>{startTime, x.first});
        startTime = INT_MAX;
      }
    }
    return res;
  }
};