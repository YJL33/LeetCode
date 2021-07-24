#include <iostream>
#include <queue>
#include <vector>

using namespace std;

// naive approach
// for all buildings, collect all its corners
// sort by x value
// 
class Solution {
public:
  vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
    // collect all events
    // differentiate left and right side of buildings
    vector<vector<int>> events;
    for (auto b:buildings) {
      events.push_back(vector<int>{b[0], b[2], 1});
      events.push_back(vector<int>{b[1], b[2], 0});
    }

    // sort by x value
    sort(events.begin(), events.end(), [](const vector<int>& a, const vector<int>& b) {return a[0] < b[0];});

    // create 2 heaps (left and right side of building)
    priority_queue<int> hp;
    priority_queue<int> toRmv;
    vector<vector<int>> skyline;
    for (auto e: events) {
      if (e[2] == 1) {
        hp.push(e[1]);
      } else {
        toRmv.push(e[1]);
      }
      // offset the left and right side (if same height)
      while (!toRmv.empty() && toRmv.top() == hp.top()) {
        hp.pop();
        toRmv.pop();
      }

      // maintain the skyline
      while (!skyline.empty() && skyline[skyline.size()-1][0] == e[0]) {
        skyline.pop_back();
      }
      // we push tallest left-side if exist
      if (hp.empty() || skyline.empty() || hp.top() != skyline[skyline.size()-1][1]) {
        skyline.push_back(vector<int>{e[0], hp.empty() ? 0 : hp.top()});
      }
    }
    return skyline;
  }
};