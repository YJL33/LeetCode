#include <iostream>
#include <vector>
#include <map>

using namespace std;

// an edge is a critical connection, if and only if it's not in a cycle.
// 1. create adjacency list
// 2. for each node, dfs to find cycle
// 3. if there's a cycle, mark all of them has root = x
// 4. check all edges and see if their root's are same or not.

class Solution {
public:
  map<int, vector<int>> adjMap;
  vector<int> visited;
  vector<int> entryTime;
  vector<int> low;
  int visitTime=0;
  vector<vector<int>> res;

  vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
    // create adj list  
    for (auto c: connections) {
      adjMap[c[0]].push_back(c[1]);
      adjMap[c[1]].push_back(c[0]);
    }

    visited = vector<int>(n, 0);          // track if we visited this node or not (1/0)
    entryTime = vector<int>(n, 0);        // record the entry time
    low = vector<int>(n, 0);              // all nodes has same low value in same cycle.

    // dfs to complete above vectors
    for (int i=0; i<n; ++i) {
      if (visited[i] == 0) {
        dfs(i, i);
      }
    }
    return res;
  }

  // mark this node as visited, and
  void dfs(int x, int parent) {
    visited[x] = 1;
    entryTime[x] = visitTime;
    low[x] = visitTime;
    for (auto nb: adjMap[x]) {
      if (nb != parent) {                   // don't go back
        if (visited[nb] == 0) {
          visitTime += 1;
          dfs(nb, x);                       // visit its children
        }
        low[x] = min(low[x], low[nb]);      // update low value if there's a cycle
        if (low[nb] > entryTime[x]) {       // add critical edges (back edge is not found)
          res.push_back(vector<int>{x, nb});
        }
      }
    }
    return;
  }
};

int main() {
  // int numOfEdge = 4;
  int numOfEdge;
  int cnt = 0;
  cin >> numOfEdge;
  vector<vector<int>> edges;
  // edges.push_back(vector<int>{1,0});
  // edges.push_back(vector<int>{2,0});
  // edges.push_back(vector<int>{1,2});
  // edges.push_back(vector<int>{1,3});
  while (cnt < numOfEdge) {
    int a, b;
    cin >> a;
    cin >> b;
    edges.push_back(vector<int>{a,b});
    cnt++;
  }
  cout << "size of edges:" << edges.size() << "    numOfEdge:" << numOfEdge << endl;
  vector<vector<int>> res = Solution().criticalConnections(numOfEdge, edges);
  cout << res.size() << endl;
}