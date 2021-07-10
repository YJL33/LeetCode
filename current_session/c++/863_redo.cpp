#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  map<int, vector<int> > connections;
  vector<int> distanceK(TreeNode* root, TreeNode* target, int k) {
    // Build connections first
    buildConnections(NULL, root);

    // BFS
    queue<int> queue;
    queue.push(target->val);
    set<int> visited;
    visited.insert(target->val);
    int dist = 0;
    vector<int> res;
    while (dist<k) {
      int numOfNodesInLayer = queue.size();
      // check the map, pop all nodes in this layer, and push all unvisited nb into queue.
      // for each node in this layer
      while (numOfNodesInLayer--) {
        int cur = queue.front(); queue.pop();
        for (int i = 0; i<connections[cur].size(); i++) {
          int neighbor = connections[cur][i];
          if (visited.find(neighbor) == visited.end()) {
            visited.insert(neighbor);
            queue.push(neighbor);
          }
        }
      }
      dist += 1;
    }
    while (!queue.empty()) {
      res.push_back(queue.front());
      queue.pop();
    }
    return res;
  }
private:
  void buildConnections(TreeNode* parent, TreeNode* child) {
    if (parent!=NULL) {
      connections[parent->val].push_back(child->val);
      connections[child->val].push_back(parent->val);
    }
    if (child->left != nullptr) buildConnections(child, child->left);
    if (child->right != nullptr) buildConnections(child, child->right);
  }
};