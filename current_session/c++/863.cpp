#include <iostream>
#include <vector>
#include <map>
#include <set>

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
    vector<int> stack{target->val};
    vector<int>* stackPtr = &stack;
    set<int> visited{target->val};
    int dist = 0;
    while (dist < k) {
      vector<int> tmp{};
      // while ((*stackPtr).size() > 0) {
      for (int j =0; j<(*stackPtr).size(); j++) {
        for (int i = 0; i < connections[(*stackPtr)[j]].size(); i++) {
          if (visited.count(connections[(*stackPtr)[j]][i]) != 0) {
            tmp.push_back(connections[(*stackPtr)[j]][i]);
            visited.insert(connections[(*stackPtr)[j]][i]);
          }
        }
        (*stackPtr).pop_back();
      }
      stackPtr = &tmp;
      dist += 1;
    }
    return stack;
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