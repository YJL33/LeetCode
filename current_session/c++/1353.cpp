#include <iostream>
#include <vector>
#include <queue>

using namespace std;

// use heap (priority queue)
// join the event that finished earliest first
// sort the events as well

// psuedo code
// for e in events:
//    hp.heappush(e)
// for d in days:
//    pop expired dates
//    join the event (cnt += 1)
// return count

// clang++ -std=c++17 c++/1353.cpp -o 1353 && ./1353 -v

class Solution {
public:
  int maxEvents(vector<vector<int>>& events) {
    priority_queue<vector<int>> pq;
    for (auto e:events) {
      pq.push({-1*e[0],-1*e[1]});         // start-day, end-day
    }
    // get the day span
    int days = 0;
    for (int i = 0; i < events.size(); ++i) {
      days = max(days, events[i][1]);
    }

    int count = 0;
    // maintain 2nd pq that using end day as priority
    priority_queue<vector<int>> pq2;      // end-day , start-day
    for (int d = 0; d <= days; ++d) {
      // move the started events from pq1 into pq2
      while (pq.size() > 0 && pq.top()[0]*-1 <= d) {
        pq2.push({pq.top()[1], pq.top()[0]});
        pq.pop();
      }
      // purge the expired events (in pq2)
      while (pq2.size() > 0 && pq2.top()[0]*-1 < d) {
        pq2.pop();
      }
      // join the event that finish earliest (in pq2)
      if (pq2.size() > 0 && pq2.top()[1]*-1 <= d) {
        pq2.pop();
        count += 1;
      }
      if (pq.size() == 0 && pq2.size() == 0) {
        break;
      }
    }
    return count;
  }
};

int main() {
  // priority_queue<vector<int>> pq;
  vector<vector<int>> test = {{2,3},{4,5},{1,2},{1,6},{3,4}};
  vector<vector<int>> test2 = {{2,3},{1,2},{1,2},{3,4}};
  vector<vector<int>> test3 = {{3,4},{2,2},{4,4},{1,4},{1,1}};
  vector<vector<int>> test4 = {{1,100000}};
  vector<vector<int>> test5 = {{1,2},{1,3},{1,4},{1,5},{1,1},{1,6},{1,7}};
  vector<vector<int>> test6 = {{2,3},{2,3},{1,5},{1,5},{1,5}};

  // for (auto e: test) {
  //   pq.push({-1*e[0], -1*e[1]});
  // }
  // while (pq.size() != 0) {
  //   cout << -1*pq.top()[0] << -1*pq.top()[1] << endl;
  //   pq.pop();
  // }
  cout << Solution().maxEvents(test) << endl;
  cout << Solution().maxEvents(test2) << endl;
  cout << Solution().maxEvents(test3) << endl;
  cout << Solution().maxEvents(test4) << endl;
  cout << Solution().maxEvents(test5) << endl;
  cout << Solution().maxEvents(test6) << endl;
}